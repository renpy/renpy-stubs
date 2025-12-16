import subprocess
import sys
import shutil
import os
from pathlib import Path

from .config import config
from .relative_imports import main as add_relative_imports


#####################
## STUB GENERATION


def generate_stubs() -> list[str]:
    """Generates .pyi stub files using stubgen and moves them to the target directory."""
    _clean_temp_dir()

    created_files: list[str] = []

    for source, target in config.renpy_directory_mapping.items():
        source_path = config.renpy_path / source
        target_path = config.pyi_path / target

        _run_command(["stubgen", "--output", str(config.temp_path), str(source_path)])
        new_files = _move_stubs(source_path, target_path)
        created_files.extend(new_files)

    _clean_temp_dir()

    return created_files


def _move_stubs(source_path: Path, target_path: Path) -> list[str]:
    stubgen_output_path = config.temp_path / source_path.name

    if not stubgen_output_path.exists():
        print(
            f"[ERROR] stubgen did not create expected output directory: {stubgen_output_path}",
            file=sys.stderr,
        )
        sys.exit(4)

    if target_path.exists():
        if target_path.is_dir():
            shutil.rmtree(target_path)
        else:
            os.remove(target_path)

    # Exclude specific files if needed
    for fn in config.exclude_files:
        path_to_exclude = (config.temp_path / fn).with_suffix(".pyi")
        if path_to_exclude.exists():
            if path_to_exclude.is_dir():
                shutil.rmtree(path_to_exclude)
            else:
                os.remove(path_to_exclude)

    os.rename(str(stubgen_output_path), str(target_path))
    return [str(p) for p in target_path.glob("**/*.pyi")]


###################
## CLEANUP


def clean_generated_files(files: list[str]) -> None:
    """Removes specific lines or artifacts from generated files."""
    for fn in files:
        try:
            with open(fn, "r", encoding="utf-8") as f:
                lines = f.readlines()

            with open(fn, "w", encoding="utf-8") as f:
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


def _clean_temp_dir():
    if os.path.exists(config.temp_path):
        shutil.rmtree(config.temp_path)


def main():
    created_files = generate_stubs()
    clean_generated_files(created_files)
    add_relative_imports()
    format_code()


if __name__ == "__main__":
    main()
