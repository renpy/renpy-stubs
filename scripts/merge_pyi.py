import os
import sys
from pathlib import Path
from typing import Optional, List, Tuple

from pytype.tools.merge_pyi.merge_pyi import merge_files, Mode
from tqdm import tqdm
from .config import config


def resolve_target_path(source_pyi_path: Path, source_root: Path, target_root: Path) -> Optional[Path]:
    """
    Determines the corresponding .py or .pyi file in the target directory.
    Handles the specific logic of removing '-stubs' suffixes from directory names.
    """
    # Calculate relative path from the source root
    relative_path = source_pyi_path.relative_to(source_root)
    parts = list(relative_path.parts)

    # Specific logic: Remove "-stubs" suffix from the top-level directory if present
    if parts and parts[0].endswith("-stubs"):
        parts[0] = parts[0].removesuffix("-stubs")

    rel_target_dir = Path(*parts).parent
    filename = source_pyi_path.name

    # Check for .py file first
    target_py = (target_root / rel_target_dir / filename).with_suffix(".py")
    if target_py.exists():
        return target_py

    # Fallback to .pyi file
    target_pyi = (target_root / rel_target_dir / filename).with_suffix(".pyi")
    if target_pyi.exists():
        return target_pyi

    return None


def clean_type_comments(file_path: Path) -> None:
    """
    Removes legacy '# type:' comments (excluding '# type: ignore') from the file.
    These comments can interfere with stubgen/merge tools.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        modified = False
        new_lines = []
        for line in lines:
            if "# type:" in line and "# type: ignore" not in line:
                # Strip the comment but keep the code
                line = line.split("# type:")[0].rstrip() + "\n"
                modified = True
            new_lines.append(line)

        if modified:
            with open(file_path, "w", encoding="utf-8") as f:
                f.writelines(new_lines)

    except IOError as e:
        print(f"[WARNING] Could not clean type comments in {file_path}: {e}", file=sys.stderr)


def collect_source_files(source_dir: Path) -> List[Path]:
    """Recursively finds all .pyi files in the source directory."""
    pyi_files = []
    for root, _, files in os.walk(source_dir):
        root_path = Path(root)
        for fn in files:
            if fn.endswith(".pyi"):
                pyi_files.append(root_path / fn)
    return pyi_files


def process_merge(source_pyi: Path, target_py: Path) -> bool:
    """
    Merges the source .pyi file into the target .py file.
    Returns True if successful, False otherwise.
    """
    try:
        clean_type_comments(target_py)
        merge_files(pyi_path=str(source_pyi), py_path=str(target_py), mode=Mode.OVERWRITE)
        return True
    except Exception as e:
        print(f"[ERROR] merging {source_pyi} -> {target_py}: {e}", file=sys.stderr)
        return False


def main():
    source_files = collect_source_files(config.pyi_path)
    progress_bar = tqdm(source_files)

    for source_pyi in progress_bar:
        target_py = resolve_target_path(source_pyi, config.pyi_path, config.renpy_path)

        if not target_py:
            # Construct a display path for the warning
            rel_path = source_pyi.relative_to(config.pyi_path)
            print(f"Skipping (no matching .py or .pyi file): {rel_path}", file=sys.stderr)
            continue

        # Update progress bar description
        display_name = target_py.relative_to(config.renpy_path)
        progress_bar.set_description(f"{str(display_name):20.20}")

        process_merge(source_pyi.resolve(), target_py.resolve())


if __name__ == "__main__":
    main()
