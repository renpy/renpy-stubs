import ast
import dataclasses
import subprocess
import sys
import shutil
import os
from pathlib import Path

from config import config
from .relative_imports import main as add_relative_imports
from .cherrypick_pyi import cherrypick_merge_file


#####################
## STUB GENERATION


@dataclasses.dataclass
class StubFileContext:
    source_python_files: list[str]
    stubgen_output_path: Path


def extract_py_from_rpy() -> None:
    cmd = [config.renpy_python, "./scripts/extract_py_from_rpy.py"]
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

        source_files = [str(Path(dirpath) / f) for f in filenames if f.endswith(".py")]
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

    # Move files from source to target, cherrypicking where hand-edited stubs exist.
    # Generated stubs live under a "renpy/" module prefix (e.g. temp/gen/renpy/renpy/atl.pyi)
    # but hand-edited stubs are at the target root (e.g. src/renpy-stubs/atl.pyi).
    # We strip the "renpy/" prefix to find the corresponding hand-edited stub.
    moved_files = []
    for src in source_path.rglob("*.pyi"):
        rel = src.relative_to(source_path)
        parts = list(rel.parts)

        # Strip the "renpy/" module prefix from the path
        if parts and parts[0] == "renpy":
            curr_rel = Path(*parts[1:])
        else:
            curr_rel = rel

        dst = target_path / curr_rel
        dst.parent.mkdir(parents=True, exist_ok=True)

        curr_path = target_path / curr_rel
        if curr_path.exists():
            # Cherrypick merge: hand=existing, gen=src(new)
            try:
                merged = cherrypick_merge_file(curr_path, src)
                curr_path.write_text(merged, encoding="utf-8")
                print(f"  Merged: {curr_rel}", file=sys.stderr)
                moved_files.append(str(curr_path))
            except Exception as e:
                print(f"  [WARNING] Cherrypick merge failed for {curr_rel}: {e}", file=sys.stderr)
                print(f"  Copying generated file as fallback", file=sys.stderr)
                shutil.copy2(str(src), str(dst))
                moved_files.append(str(dst))
        else:
            shutil.copy2(str(src), str(dst))
            moved_files.append(str(dst))

    shutil.rmtree(str(source_path))

    # Remove empty files
    for p in target_path.glob("**/*.pyi"):
        if p.stat().st_size == 0:
            p.unlink()

    return moved_files


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
    # ruff check --fix returns exit code 1 when issues are found
    # (even if they were fixed). This is not a fatal error.
    try:
        _run_command(["ruff", "check", str(config.pyi_path), "--fix"])
    except SystemExit as e:
        if e.code != 1:
            raise
    _run_command(["ruff", "format", str(config.pyi_path)])


###################
## HELPERS


def _find_tool(tool: str) -> str:
    """
    Locates an executable tool (e.g. 'ruff', 'stubgen') without modifying PATH.
    Resolution order:
    1. PATH (shutil.which)
    2. Next to the running Python: <python_dir>/Scripts/<tool>.exe on Windows,
       <python_dir>/<tool> on POSIX.
    Raises FileNotFoundError if the tool cannot be found.
    """
    import shutil

    found = shutil.which(tool)
    if found:
        return found

    python_dir = Path(sys.executable).parent
    if os.name == "nt":
        candidates = [
            python_dir / "Scripts" / f"{tool}.exe",
            python_dir / f"{tool}.exe",
        ]
    else:
        candidates = [
            python_dir / tool,
            python_dir.parent / "bin" / tool,
        ]

    for candidate in candidates:
        if candidate.is_file():
            return str(candidate)

    raise FileNotFoundError(
        f"Could not find '{tool}'. Install it with `uv sync`."
    )


def _run_command(cmd: list[str]) -> None:
    # Resolve the tool executable so it works even when the interpreter's
    # Scripts/bin directory is not on PATH (common with conda environments).
    # Only resolve simple names (no path separators) -- skip paths and relative paths.
    import os.path

    first = cmd[0]
    if os.path.sep not in first and (os.path.altsep is None or os.path.altsep not in first):
        first = _find_tool(first)
    resolved = [first] + cmd[1:]

    try:
        completed = subprocess.run(resolved, check=False)
    except FileNotFoundError as e:
        print(f"[ERROR] {e}", file=sys.stderr)

        suggestion = ""
        if cmd[0] in ("ruff", "stubgen"):
            suggestion = "uv sync"

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
    # Remove the stale generated-stubs directory from previous runs
    # (e.g. src/renpy-stubs/renpy/). Generated stubs are now merged into
    # the hand-edited stubs at the target root, so this subdirectory is obsolete.
    path = config.pyi_path / "renpy-stubs" / "renpy"
    if path.exists():
        shutil.rmtree(path)
    # Also clean the legacy path if it somehow exists
    path = config.pyi_path / "renpy"
    if path.exists():
        shutil.rmtree(path)


def _clean_temp_dir():
    if config.rpy_extraction_temp_path.exists():
        shutil.rmtree(config.rpy_extraction_temp_path)
    if config.temp_gen_path.exists():
        shutil.rmtree(config.temp_gen_path)


def main():
    _clean_temp_dir()
    _remove_existing_directory()

    extract_py_from_rpy()
    created_files = generate_stubs()

    _clean_temp_dir()
    clean_generated_files(created_files)
    add_relative_imports()
    format_code()


if __name__ == "__main__":
    main()
