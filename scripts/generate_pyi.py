import ast
import dataclasses
import subprocess
import sys
import shutil
import os
from pathlib import Path

from .config import config
from .relative_imports import main as add_relative_imports


#####################
## STUB GENERATION


@dataclasses.dataclass
class StubFileContext:
    source_python_files: list[str]
    stubgen_output_path: Path


def extract_py_from_rpy() -> None:
    cmd = ["../renpy-8.5.0-sdk/lib/py3-windows-x86_64/python.exe", "./scripts/extract_py_from_rpy.py"]
    _run_command(cmd)


def generate_stubs() -> list[str]:
    """Generates .pyi stub files using stubgen and moves them to the target directory."""
    stub_file_contexts: list[StubFileContext] = []

    # Generate stubs for Ren'Py codebase
    stub_file_contexts.append(
        StubFileContext(
            source_python_files=[str(config.renpy_path / "renpy")],
            stubgen_output_path=config.temp_gen_path,
        )
    )

    # Generate stubs for extracted .rpy files
    for dirpath, _, filenames in os.walk(config.rpy_extraction_temp_path):
        extracted_name = Path(dirpath).relative_to(config.rpy_extraction_temp_path)
        if len(extracted_name.parts) < 2 or extracted_name.parts[0] != "renpy":
            continue
        extracted_name = extracted_name.relative_to("renpy")

        source_files = [os.path.join(dirpath, f) for f in filenames if f.endswith(".py")]
        if not source_files:
            continue

        stub_file_contexts.append(
            StubFileContext(
                source_python_files=source_files,
                stubgen_output_path=config.temp_gen_path / "renpy" / extracted_name,
            )
        )

    for ctx in stub_file_contexts:
        _run_command([
            "stubgen",
            "--include-private",
            "--output",
            str(ctx.stubgen_output_path),
            *ctx.source_python_files,
        ])

    created_files = _move_stubs(config.temp_gen_path / "renpy", config.pyi_path / "renpy-stubs")
    return created_files


def _move_stubs(source_path: Path, target_path: Path) -> list[str]:
    if not source_path.exists():
        print(
            f"[ERROR] stubgen did not create expected output directory: {source_path}",
            file=sys.stderr,
        )
        sys.exit(4)

    # Exclude specific files if needed
    for fn in config.exclude_files:
        path_to_exclude = config.temp_gen_path / fn

        if path_to_exclude.exists() and path_to_exclude.is_dir():
            shutil.rmtree(path_to_exclude)
        else:
            path_to_exclude = path_to_exclude.with_suffix(".pyi")
            if path_to_exclude.exists():
                os.remove(path_to_exclude)

    shutil.copytree(str(source_path), str(target_path), dirs_exist_ok=True)
    shutil.rmtree(str(source_path))

    for p in target_path.glob("**/*.pyi"):
        if os.path.getsize(p) == 0:
            os.remove(str(p))

    return [str(p) for p in target_path.glob("**/*.pyi")]


###################
## CLEANUP


def clean_generated_files(files: list[str]) -> None:
    """Removes specific lines or artifacts from generated files."""
    for fn in files:
        try:
            with open(fn, "r", encoding="utf-8") as f:
                lines = f.readlines()

            with open(fn, "w", encoding="utf-8", newline="\n") as f:
                for line in lines:
                    if line.startswith("from renpy.compat import"):
                        continue
                    f.write(line)
        except Exception as e:
            print(f"[WARNING] failed to clean up file '{fn}': {e}", file=sys.stderr)


#####################
## FORMATTING


def format_code() -> None:
    """Runs ruff to check and format generated .pyi files."""
    _run_command(["ruff", "check", str(config.pyi_path), "--fix"])
    _run_command(["ruff", "format", str(config.pyi_path)])


###################
## HELPERS


def _run_command(cmd: list[str]) -> None:
    try:
        completed = subprocess.run(cmd, check=False)
    except FileNotFoundError as e:
        print(f"[ERROR] {e}", file=sys.stderr)

        suggestion = ""
        if cmd[0] == "ruff":
            suggestion = "pip install ruff"
        elif cmd[0] == "stubgen":
            suggestion = "pip install mypy"

        if suggestion:
            print(
                f"If {cmd[0]} was not found, try `{suggestion}` or ensure '{cmd[0]}' is on PATH.",
                file=sys.stderr,
            )
        return

    if completed.returncode != 0:
        print(
            f"[ERROR] `{' '.join(cmd)}` failed with exit code {completed.returncode}",
            file=sys.stderr,
        )
        sys.exit(completed.returncode)


def _remove_existing_directory():
    path = config.pyi_path / "renpy"
    if path.exists():
        shutil.rmtree(path)


def _clean_temp_dir():
    if os.path.exists(config.rpy_extraction_temp_path):
        shutil.rmtree(config.rpy_extraction_temp_path)
    if os.path.exists(config.temp_gen_path):
        shutil.rmtree(config.temp_gen_path)


def main():
    _clean_temp_dir()
    # _remove_existing_directory()

    extract_py_from_rpy()
    created_files = generate_stubs()

    _clean_temp_dir()
    clean_generated_files(created_files)
    add_relative_imports()
    format_code()


if __name__ == "__main__":
    main()
