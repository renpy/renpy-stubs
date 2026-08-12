import os
import sys
import re
import ast
import subprocess
from pathlib import Path
from typing import Optional, List, Set
import traceback

from pytype.tools.merge_pyi.merge_pyi import merge_files, Mode
from config import config


def resolve_target_path(source_pyi_path: Path, source_root: Path, target_root: Path) -> Optional[Path]:
    """
    Determines the corresponding .py or .pyi file in the target directory.
    Handles the specific logic of removing '-stubs' suffixes from directory names.
    """
    relative_path = source_pyi_path.relative_to(source_root)
    parts = list(relative_path.parts)

    if parts and parts[0].endswith("-stubs"):
        parts[0] = parts[0].removesuffix("-stubs")

    rel_target_dir = Path(*parts).parent
    filename = source_pyi_path.name

    target_py = (target_root / rel_target_dir / filename).with_suffix(".py")
    if target_py.exists():
        return target_py

    target_pyi = (target_root / rel_target_dir / filename).with_suffix(".pyi")
    if target_pyi.exists():
        return target_pyi

    return None


def clean_type_comments(file_path: Path) -> None:
    """Removes bare `# type:` comments (but not `# type: ignore`). Preserves line endings."""
    try:
        with open(file_path, "r", encoding="utf-8", errors="replace", newline="") as f:
            content = f.read()
    except IOError as e:
        print(f"[WARNING] Could not clean type comments in {file_path}: {e}", file=sys.stderr)
        return

    # Detect line ending style
    if "\r\n" in content:
        eol = "\r\n"
    else:
        eol = "\n"

    lines = content.splitlines(keepends=True)
    modified = False
    new_lines = []
    for line in lines:
        if "# type:" in line and "# type: ignore" not in line:
            line = line.split("# type:")[0].rstrip() + eol
            modified = True
        new_lines.append(line)

    if modified:
        try:
            with open(file_path, "w", encoding="utf-8", newline="") as f:
                f.writelines(new_lines)
        except IOError as e:
            print(f"[WARNING] Could not write cleaned file {file_path}: {e}", file=sys.stderr)


def collect_source_files(source_dir: Path) -> List[Path]:
    pyi_files = []
    for root, _, files in os.walk(source_dir):
        root_path = Path(root)
        for fn in files:
            if fn.endswith(".pyi"):
                pyi_files.append(root_path / fn)
    return pyi_files


_STDLIB_MODULES: Set[str] = {
    "__future__",
    "_thread",
    "abc",
    "ast",
    "asyncio",
    "base64",
    "binascii",
    "bisect",
    "builtins",
    "bz2",
    "calendar",
    "collections",
    "concurrent",
    "configparser",
    "contextlib",
    "copy",
    "copyreg",
    "csv",
    "ctypes",
    "dataclasses",
    "datetime",
    "decimal",
    "difflib",
    "dis",
    "email",
    "enum",
    "errno",
    "faulthandler",
    "functools",
    "gc",
    "getopt",
    "gettext",
    "glob",
    "grp",
    "gzip",
    "hashlib",
    "heapq",
    "hmac",
    "html",
    "http",
    "importlib",
    "inspect",
    "io",
    "itertools",
    "json",
    "keyword",
    "linecache",
    "locale",
    "logging",
    "lzma",
    "marshal",
    "math",
    "mmap",
    "multiprocessing",
    "netrc",
    "operator",
    "optparse",
    "os",
    "pathlib",
    "pickle",
    "pickletools",
    "platform",
    "plistlib",
    "pprint",
    "profile",
    "pstats",
    "pty",
    "pwd",
    "py_compile",
    "pyclbr",
    "pydoc",
    "queue",
    "quopri",
    "random",
    "re",
    "readline",
    "reprlib",
    "resource",
    "runpy",
    "sched",
    "secrets",
    "select",
    "selectors",
    "shelve",
    "shlex",
    "shutil",
    "signal",
    "site",
    "smtpd",
    "smtplib",
    "sndhdr",
    "socket",
    "socketserver",
    "sqlite3",
    "ssl",
    "stat",
    "statistics",
    "string",
    "stringprep",
    "struct",
    "subprocess",
    "sys",
    "sysconfig",
    "tabnanny",
    "tarfile",
    "tempfile",
    "textwrap",
    "threading",
    "time",
    "timeit",
    "token",
    "tokenize",
    "trace",
    "traceback",
    "tracemalloc",
    "tty",
    "types",
    "typing",
    "unicodedata",
    "unittest",
    "urllib",
    "uu",
    "uuid",
    "warnings",
    "wave",
    "weakref",
    "webbrowser",
    "xml",
    "zipapp",
    "zipfile",
    "zipimport",
    "zlib",
    "_typeshed",
    "collections.abc",
    "contextvars",
    "dataclasses",
    "enum",
    "re",
    "typing_extensions",
}


def _extract_imports(source: str) -> Set[str]:
    """Extract top-level module import names from source code."""
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return set()

    imports: Set[str] = set()
    for node in tree.body:
        if isinstance(node, ast.Import):
            for alias in node.names:
                imports.add(alias.name.split(".")[0])
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                imports.add(node.module.split(".")[0])
    return imports


_TYPING_NAMES: Set[str] = {
    "Self",
    "Any",
    "Callable",
    "Generator",
    "Iterable",
    "Iterator",
    "Optional",
    "Union",
    "TypeVar",
    "ParamSpec",
    "Generic",
    "Protocol",
    "Literal",
    "Final",
    "TypeAlias",
    "TypeGuard",
    "Never",
    "NoReturn",
    "TYPE_CHECKING",
    "overload",
    "Concatenate",
}


def _fix_typing_annotation_imports(file_path: Path) -> None:
    """
    Add missing typing imports for bare annotation names like `Self` that
    the merge tool may have introduced without the corresponding import.
    """
    try:
        with open(file_path, "r", encoding="utf-8", errors="replace", newline="") as f:
            source = f.read()
    except (UnicodeDecodeError, IOError) as e:
        print(f"[WARNING] Could not read {file_path} for typing fix: {e}", file=sys.stderr)
        return

    # Detect line ending style
    if "\r\n" in source:
        eol = "\r\n"
    else:
        eol = "\n"

    try:
        tree = ast.parse(source)
    except SyntaxError:
        return

    # Check what typing names are already imported
    imported_typing_names: Set[str] = set()
    has_import_typing = False
    has_from_typing_import = False

    for node in tree.body:
        if isinstance(node, ast.Import):
            for alias in node.names:
                if alias.name == "typing" or alias.name.startswith("typing."):
                    has_import_typing = True
        elif isinstance(node, ast.ImportFrom):
            if node.module == "typing" or node.module == "typing_extensions":
                has_from_typing_import = True
                for alias in node.names:
                    imported_typing_names.add(alias.asname or alias.name)

    # Find bare typing names used in annotations, decorators, and assignments
    used_typing_names: Set[str] = set()

    # Check function return annotations, decorators, class bases
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            if node.returns is not None:
                _collect_annotation_names(node.returns, used_typing_names)
            for decorator in node.decorator_list:
                if isinstance(decorator, ast.Name):
                    used_typing_names.add(decorator.id)
                elif isinstance(decorator, ast.Attribute):
                    used_typing_names.add(decorator.attr)
        elif isinstance(node, ast.ClassDef):
            for decorator in node.decorator_list:
                if isinstance(decorator, ast.Name):
                    used_typing_names.add(decorator.id)
                elif isinstance(decorator, ast.Attribute):
                    used_typing_names.add(decorator.attr)
            for base in node.bases:
                if isinstance(base, ast.Name):
                    used_typing_names.add(base.id)
                elif isinstance(base, ast.Subscript):
                    _collect_annotation_names(base, used_typing_names)
        elif isinstance(node, ast.Assign):
            # Check for TypeVar("T"), ParamSpec("P") etc.
            if isinstance(node.value, ast.Call):
                if isinstance(node.value.func, ast.Name):
                    used_typing_names.add(node.value.func.id)
        elif isinstance(node, ast.AnnAssign):
            if node.annotation is not None:
                _collect_annotation_names(node.annotation, used_typing_names)

    # Filter to known typing names
    # If `import typing` is present, bare names like `TypeVar` won't work
    # unless they're also imported via `from typing import TypeVar`
    missing = (used_typing_names & _TYPING_NAMES) - imported_typing_names
    if not missing:
        return

    # Add the import
    lines = source.splitlines(keepends=True)
    insert_at = 0
    while insert_at < len(lines):
        stripped = lines[insert_at].lstrip()
        if stripped.startswith("#"):
            insert_at += 1
            continue
        break

    if insert_at < len(lines) and (
        lines[insert_at].lstrip().startswith('"""') or lines[insert_at].lstrip().startswith("'''")
    ):
        quote = lines[insert_at].lstrip()[:3]
        for i in range(insert_at, len(lines)):
            if lines[i].count(quote) >= 2 or (i > insert_at and quote in lines[i]):
                insert_at = i + 1
                break

    # Find the right place to insert (after __future__ imports, before other imports)
    for i in range(insert_at, len(lines)):
        stripped = lines[i].lstrip()
        if stripped.startswith("from __future__"):
            insert_at = i + 1
            continue
        break

    new_import = f"from typing import {', '.join(sorted(missing))}{eol}"
    lines.insert(insert_at, new_import)

    if insert_at > 0 and not lines[insert_at - 1].endswith(eol * 2):
        lines.insert(insert_at, eol)

    # print(f"  Added missing typing imports: {', '.join(sorted(missing))}", file=sys.stderr)

    try:
        with open(file_path, "w", encoding="utf-8", newline="") as f:
            f.writelines(lines)
    except IOError as e:
        print(f"[WARNING] Could not write typing imports to {file_path}: {e}", file=sys.stderr)


def _collect_annotation_names(node: ast.AST, names: Set[str]) -> None:
    """Collect bare Name nodes from an annotation AST."""
    if isinstance(node, ast.Name):
        names.add(node.id)
    elif isinstance(node, ast.Subscript):
        _collect_annotation_names(node.value, names)
        if isinstance(node.slice, ast.AST):
            _collect_annotation_names(node.slice, names)
    elif isinstance(node, ast.Tuple):
        for elt in node.elts:
            _collect_annotation_names(elt, names)
    elif isinstance(node, ast.Attribute):
        # typing.Self - don't add 'Self' since it's qualified
        pass
    elif isinstance(node, ast.Constant):
        pass  # String literal forward refs
    elif isinstance(node, ast.BinOp):
        _collect_annotation_names(node.left, names)
        _collect_annotation_names(node.right, names)


def _is_import_used(source: str, module: str, names: Set[str]) -> bool:
    """Check if any of the imported names are actually used in the source code."""
    for name in names:
        # Check for bare usage of the name
        if name in source:
            # Make sure it's not just part of the import itself
            # (we check for the import separately)
            lines = source.splitlines()
            for line in lines:
                stripped = line.strip()
                # Skip the import line itself
                if re.match(rf"^\s*from\s+{re.escape(module)}\s+import", stripped):
                    continue
                if re.match(rf"^\s*import\s+{re.escape(name)}(?:\s|$|,)", stripped):
                    continue
                # Check if name appears in the line
                if name in stripped:
                    return True
    return False


def _restore_original_imports(merged_path: Path, original_source: str) -> None:
    """
    Removes imports that were added by the merge but are not in the original
    and are not stdlib / renpy modules. These are typically polluted variable
    names that pytype mistakenly merged as module imports.
    """
    try:
        with open(merged_path, "r", encoding="utf-8", errors="replace", newline="") as f:
            merged_source = f.read()
    except (UnicodeDecodeError, IOError) as e:
        print(f"[WARNING] Could not read merged file {merged_path}: {e}", file=sys.stderr)
        return

    original_imports = _extract_imports(original_source)
    merged_imports = _extract_imports(merged_source)

    new_imports = merged_imports - original_imports

    polluted_imports = {
        imp
        for imp in new_imports
        if imp not in _STDLIB_MODULES and imp != "_typeshed" and not (imp == "renpy" or imp.startswith("renpy."))
    }

    if not polluted_imports:
        return

    lines = merged_source.splitlines(keepends=True)
    new_lines = []
    removed = set()

    for line in lines:
        stripped = line.strip()
        is_polluted = False
        for imp in polluted_imports:
            if stripped == f"import {imp}":
                # Only remove TOP-LEVEL imports (not indented ones inside try/if blocks)
                if not line.startswith((" ", "\t")):
                    is_polluted = True
                    removed.add(imp)
                    break
                break
            if (stripped.startswith(f"from {imp} ") or stripped.startswith(f"from {imp}.")) and not (
                imp == "renpy" or imp.startswith("renpy.")
            ):
                # Only remove TOP-LEVEL imports
                if not line.startswith((" ", "\t")):
                    is_polluted = True
                    removed.add(imp)
                    break
                break
        if not is_polluted:
            new_lines.append(line)

    # if removed:
    #     print(f"  Removed polluted imports: {', '.join(sorted(removed))}", file=sys.stderr)

    try:
        with open(merged_path, "w", encoding="utf-8", newline="") as f:
            f.writelines(new_lines)
    except IOError as e:
        print(f"[WARNING] Could not write cleaned file {merged_path}: {e}", file=sys.stderr)


def _extract_import_details(source: str) -> list[tuple[str, str, list[str]]]:
    """
    Extract detailed import info from source.
    Returns list of (type, module, names) tuples:
      - type: 'import' or 'from'
      - module: the module name
      - names: list of imported names (for 'from' imports) or ['*'] for 'import'
    """
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return []

    result: list[tuple[str, str, list[str]]] = []
    for node in tree.body:
        if isinstance(node, ast.Import):
            for alias in node.names:
                result.append(("import", alias.name, [alias.asname or alias.name]))
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                names = [alias.asname or alias.name for alias in node.names]
                result.append(("from", node.module, names))
    return result


def _is_import_used_at_runtime(source: str, tree: ast.AST, mod: str, names: tuple[str, ...]) -> bool:
    """
    Check if any of the imported names are used at RUNTIME (not just in annotations).
    Uses AST to find all annotation contexts, then checks if the name appears
    in the source outside those contexts.
    """
    import ast as _ast

    # Find all annotation text ranges (line:col_start to line:col_end)
    # These are locations where the name is used in annotations and won't be
    # evaluated at runtime (with `from __future__ import annotations`).
    annotation_ranges = set()
    for node in _ast.walk(tree):
        # Variable annotations: x: Type = ...
        if isinstance(node, _ast.AnnAssign) and node.annotation is not None:
            for child in _ast.walk(node.annotation):
                if hasattr(child, "lineno") and hasattr(child, "col_offset"):
                    annotation_ranges.add((child.lineno, child.col_offset))
        # Parameter annotations: def f(x: Type, ...)
        if isinstance(node, (_ast.FunctionDef, _ast.AsyncFunctionDef)):
            all_args = list(node.args.args) + list(node.args.kwonlyargs)
            if node.args.vararg:
                all_args.append(node.args.vararg)
            if node.args.kwarg:
                all_args.append(node.args.kwarg)
            for arg in all_args:
                if arg.annotation is not None:
                    for child in _ast.walk(arg.annotation):
                        if hasattr(child, "lineno") and hasattr(child, "col_offset"):
                            annotation_ranges.add((child.lineno, child.col_offset))
            # Return annotation: def f() -> Type:
            if node.returns is not None:
                for child in _ast.walk(node.returns):
                    if hasattr(child, "lineno") and hasattr(child, "col_offset"):
                        annotation_ranges.add((child.lineno, child.col_offset))

    for name in names:
        for node in _ast.walk(tree):
            if isinstance(node, _ast.Name) and node.id == name:
                if hasattr(node, "lineno") and hasattr(node, "col_offset"):
                    key = (node.lineno, node.col_offset)
                    if key not in annotation_ranges:
                        return True  # Real runtime usage
    return False


def _fix_type_check_only_import(new_lines: list[str], has_type_checking_block: bool, eol: str) -> None:
    """
    Handle `type_check_only` in the merged file:
    - `typing.type_check_only` only exists in Python 3.14+, not in 3.12.
    - All `@type_check_only`-decorated symbols should already be moved to TYPE_CHECKING.
    - Remove `type_check_only` from top-level `from typing import` (would fail on 3.12).
    - Add `type_check_only` to the TYPE_CHECKING block's typing import if needed.
    """
    # Remove type_check_only from top-level typing import
    for i, line in enumerate(new_lines):
        stripped = line.strip()
        if stripped.startswith("from typing import") and "type_check_only" in stripped:
            parts = stripped.split("import", 1)
            if len(parts) == 2:
                names = [n.strip() for n in parts[1].split(",")]
                names = [n for n in names if n != "type_check_only"]
                if names:
                    new_line = parts[0] + "import " + ", ".join(names)
                    if not new_line.endswith(eol):
                        new_line += eol
                    new_lines[i] = new_line
                else:
                    new_lines[i] = ""
            break

    # Add type_check_only to the TYPE_CHECKING block's typing import
    if not has_type_checking_block:
        return

    for i, line in enumerate(new_lines):
        stripped = line.strip()
        if stripped.startswith("if TYPE_CHECKING"):
            for j in range(i + 1, len(new_lines)):
                inner = new_lines[j].strip()
                if not inner.startswith(("    ", "\t")):
                    break
                if inner.startswith("from typing import") and "type_check_only" not in inner:
                    if inner.endswith("\n"):
                        new_lines[j] = inner.rstrip("\n") + ", type_check_only" + eol
                    else:
                        new_lines[j] = inner + ", type_check_only" + eol
                    break
            break


def _add_type_checking_definitions(file_path: Path, source_pyi: Path) -> None:
    """
    Add type-only definitions (type aliases, classes) from the stub's
    `if TYPE_CHECKING:` blocks into the merged file's TYPE_CHECKING block.
    Pytype drops these definitions entirely, but they are needed for type checkers
    since they are referenced in annotations.
    """
    # Read the stub
    try:
        stub_source = source_pyi.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return

    # Parse the stub to find TYPE_CHECKING blocks
    try:
        stub_tree = ast.parse(stub_source)
    except SyntaxError:
        return

    stub_lines = stub_source.splitlines(keepends=True)

    # Find all definitions inside `if TYPE_CHECKING:` blocks in the stub
    type_checking_defs: list[tuple[str, int, int]] = []  # (name, start_line, end_line) 0-based

    for node in ast.walk(stub_tree):
        if isinstance(node, ast.If):
            if isinstance(node.test, ast.Name) and node.test.id == "TYPE_CHECKING":
                for item in node.body:
                    if isinstance(item, ast.ClassDef):
                        if hasattr(item, "lineno") and hasattr(item, "end_lineno"):
                            start = item.lineno - 1
                            while start > 0 and stub_lines[start - 1].strip().startswith("@"):
                                start -= 1
                            type_checking_defs.append((item.name, start, item.end_lineno))
                    elif isinstance(item, ast.TypeAlias):
                        if hasattr(item, "lineno") and hasattr(item, "end_lineno"):
                            type_checking_defs.append((item.name.id, item.lineno - 1, item.end_lineno))
                    elif isinstance(item, ast.FunctionDef):
                        if hasattr(item, "lineno") and hasattr(item, "end_lineno"):
                            start = item.lineno - 1
                            while start > 0 and stub_lines[start - 1].strip().startswith("@"):
                                start -= 1
                            type_checking_defs.append((item.name, start, item.end_lineno))
                    elif isinstance(item, ast.AnnAssign) and isinstance(item.target, ast.Name):
                        if hasattr(item, "lineno") and hasattr(item, "end_lineno"):
                            type_checking_defs.append((item.target.id, item.lineno - 1, item.end_lineno))

    if not type_checking_defs:
        return

    # Read the merged file
    try:
        merged_source = file_path.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return

    # Check which names are used in the merged file but not defined
    try:
        merged_tree = ast.parse(merged_source)
    except SyntaxError:
        return

    # Collect names defined in the merged file
    defined_names: set[str] = set()
    for node in ast.walk(merged_tree):
        if isinstance(node, ast.ClassDef):
            defined_names.add(node.name)
        elif isinstance(node, ast.FunctionDef):
            defined_names.add(node.name)
        elif isinstance(node, ast.TypeAlias):
            defined_names.add(node.name.id)
        elif isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    defined_names.add(target.id)
        elif isinstance(node, ast.AnnAssign):
            if isinstance(node.target, ast.Name):
                defined_names.add(node.target.id)

    # Also collect imported names (including from TYPE_CHECKING blocks)
    imported_names: set[str] = set()
    for node in ast.walk(merged_tree):
        if isinstance(node, ast.ImportFrom) and node.module:
            for alias in node.names:
                imported_names.add(alias.asname or alias.name)
        elif isinstance(node, ast.Import):
            for alias in node.names:
                imported_names.add(alias.asname or alias.name)

    # Find which stub TYPE_CHECKING definitions are used but not defined
    lines_to_add: list[str] = []
    added_names: list[str] = []

    for name, start, end in type_checking_defs:
        name_used = False
        for node in ast.walk(merged_tree):
            if isinstance(node, ast.Name) and node.id == name:
                name_used = True
                break

        if name_used and name not in defined_names and name not in imported_names:
            # Extract the definition lines from the stub, stripping existing indentation
            # and adding 4 spaces for the TYPE_CHECKING block
            for i in range(start, end):
                line = stub_lines[i]
                stripped_line = line.lstrip()  # Remove existing indentation
                if stripped_line or not lines_to_add:
                    lines_to_add.append(f"    {stripped_line}")
            if lines_to_add and not lines_to_add[-1].endswith("\n"):
                lines_to_add[-1] += "\n"
            added_names.append(name)

    if not lines_to_add:
        return

    # Detect line ending style
    if "\r\n" in merged_source:
        eol = "\r\n"
    else:
        eol = "\n"

    merged_lines = merged_source.splitlines(keepends=True)

    # Find the existing TYPE_CHECKING block and add definitions at the END of it
    # (after the imports, before the closing blank line)
    tc_insert_at = None
    for i, line in enumerate(merged_lines):
        stripped = line.strip()
        if stripped.startswith("if TYPE_CHECKING"):
            # Find the end of the TYPE_CHECKING block: last indented line
            last_indented = None
            for j in range(i + 1, len(merged_lines)):
                inner = merged_lines[j].strip()
                if not inner:
                    continue  # Skip blank lines within the block
                if inner.startswith(("    ", "\t")):
                    last_indented = j  # This is still inside the block
                else:
                    break  # Reached end of block
            if last_indented is not None:
                # Insert after the last indented line
                tc_insert_at = last_indented + 1
            else:
                # No indented lines in the block, insert after the colon
                tc_insert_at = i + 1
            break

    if tc_insert_at is not None:
        # Add a blank line before the definitions if the last line isn't blank
        if tc_insert_at > 0 and merged_lines[tc_insert_at - 1].strip():
            lines_to_add.insert(0, eol)
        # Also add a trailing blank line after the definitions
        if not lines_to_add[-1].endswith(eol * 2):
            lines_to_add.append(eol)
        merged_lines[tc_insert_at:tc_insert_at] = lines_to_add
        # print(f"  Added TYPE_CHECKING defs: {', '.join(added_names)}", file=sys.stderr)
    else:
        # No TYPE_CHECKING block exists - create one
        insert_at = 0
        for i, line in enumerate(merged_lines):
            stripped = line.strip()
            if not stripped or stripped.startswith("#") or stripped.startswith('"') or stripped.startswith("'"):
                insert_at = i + 1
                continue
            if stripped.startswith("import ") or stripped.startswith("from "):
                insert_at = i + 1
                continue
            break

        tc_block = [f"if TYPE_CHECKING:{eol}"]
        tc_block.extend(lines_to_add)
        tc_block.append(eol)
        merged_lines[insert_at:insert_at] = tc_block
        # print(f"  Added TYPE_CHECKING block with defs: {', '.join(added_names)}", file=sys.stderr)

    try:
        with open(file_path, "w", encoding="utf-8", newline="") as f:
            f.writelines(merged_lines)
    except IOError as e:
        print(f"[WARNING] Could not write TYPE_CHECKING defs to {file_path}: {e}", file=sys.stderr)


def _move_type_checking_imports(file_path: Path, original_source: str) -> None:
    """
    Move new renpy-internal imports AND Protocol class definitions (added by the merge)
    into a TYPE_CHECKING block to avoid circular imports at runtime.
    """
    if not original_source:
        return

    try:
        with open(file_path, "r", encoding="utf-8", errors="replace", newline="") as f:
            merged_source = f.read()
    except (UnicodeDecodeError, IOError) as e:
        print(f"[WARNING] Could not read {file_path} for TYPE_CHECKING fix: {e}", file=sys.stderr)
        return

    # Detect line ending style
    if "\r\n" in merged_source:
        eol = "\r\n"
    else:
        eol = "\n"

    # Parse both original and merged to find Protocol classes
    try:
        orig_tree = ast.parse(original_source)
    except SyntaxError:
        orig_tree = ast.parse("")

    try:
        merged_tree = ast.parse(merged_source)
    except SyntaxError:
        return  # Can't parse merged file

    # Find Protocol class definitions in original
    original_protocol_lines: set[int] = set()
    for i, node in enumerate(ast.walk(orig_tree)):
        if isinstance(node, ast.ClassDef):
            for base in node.bases:
                if (isinstance(base, ast.Name) and base.id == "Protocol") or (
                    isinstance(base, ast.Attribute) and base.attr == "Protocol"
                ):
                    if hasattr(node, "lineno"):
                        original_protocol_lines.add(node.lineno)
                    break

    # Get detailed imports from both original and merged
    original_imports = _extract_import_details(original_source)
    merged_imports = _extract_import_details(merged_source)

    # Find new imports in merged that are not in original
    original_import_set: set[tuple[str, str, tuple[str, ...]]] = set()
    for typ, mod, names in original_imports:
        original_import_set.add((typ, mod, tuple(sorted(names))))

    merged_import_set: set[tuple[str, str, tuple[str, ...]]] = set()
    for typ, mod, names in merged_imports:
        merged_import_set.add((typ, mod, tuple(sorted(names))))

    new_imports = merged_import_set - original_import_set

    # First, add `annotations` to `from __future__ import` so annotations become lazy.
    # This must happen BEFORE the "used at runtime" check below, otherwise annotation
    # types will appear to be used at runtime and won't be moved to TYPE_CHECKING.
    lines = merged_source.splitlines(keepends=True)

    found_future_import = False
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith("from __future__ import"):
            found_future_import = True
            if "annotations" not in stripped:
                import_part = stripped
                comment_part = ""
                if "  # " in stripped:
                    idx = stripped.index("  # ")
                    import_part = stripped[:idx]
                    comment_part = stripped[idx:]
                elif " #" in stripped:
                    idx = stripped.index(" #")
                    import_part = stripped[:idx]
                    comment_part = stripped[idx:]
                if import_part.endswith("\n"):
                    import_part = import_part.rstrip("\n")
                new_line = import_part + ", annotations" + comment_part
                if not new_line.endswith("\n"):
                    new_line += "\n"
                lines[i] = new_line
                # print(f"  Added 'annotations' to __future__ imports", file=sys.stderr)
            break

    if not found_future_import:
        insert_at = 0
        for i, line in enumerate(lines):
            stripped = line.strip()
            if not stripped or stripped.startswith("#"):
                insert_at = i + 1
                continue
            if stripped.startswith('"""') or stripped.startswith("'''"):
                quote = stripped[:3]
                for j in range(i, len(lines)):
                    if lines[j].count(quote) >= 2 or (j > i and quote in lines[j]):
                        insert_at = j + 1
                        break
                break
            if stripped.startswith("import ") or stripped.startswith("from "):
                break
            break
        lines.insert(insert_at, f"from __future__ import annotations\n")
        # print(f"  Added 'from __future__ import annotations'", file=sys.stderr)
        insert_at += 1

    # Update merged_source to include the __future__ annotations change for subsequent checks
    merged_source = "".join(lines)

    # Re-parse the AST with the updated __future__ annotations so annotations
    # are treated as lazy strings (ast.Constant) rather than evaluated expressions.
    try:
        merged_tree = ast.parse(merged_source)
    except SyntaxError:
        return  # Can't parse merged file

    # Filter to imports that should go in the TYPE_CHECKING block:
    #   - _typeshed: only available to type checkers
    #   - renpy.* and annotation-only stdlib imports whose names are NOT used at runtime
    # For each module, check individual names and split if needed.
    renpy_type_checking_imports: list[tuple[str, str, tuple[str, ...]]] = []
    for typ, mod, names in sorted(new_imports):
        # _typeshed is only available to type checkers - always move to TYPE_CHECKING
        if mod.startswith("_typeshed"):
            renpy_type_checking_imports.append((typ, mod, names))
            continue
        # Skip plain stdlib modules that aren't annotation helpers
        if mod in _STDLIB_MODULES and mod not in ("types", "typing_extensions", "collections.abc", "enum"):
            continue
        # Skip non-renpy, non-annotation-stdlib imports
        if not mod.startswith("renpy") and mod not in ("types", "typing_extensions", "collections.abc", "enum"):
            continue
        # Skip renpy.compat (these are already in the original and needed at runtime)
        if mod.startswith("renpy.compat"):
            continue
        # Skip plain `import renpy`
        if mod == "renpy" and typ == "import":
            continue
        # Check each name individually: some may be annotation-only, some runtime
        annotation_only_names: list[str] = []
        for name in names:
            if not _is_import_used_at_runtime(merged_source, merged_tree, mod, (name,)):
                annotation_only_names.append(name)
        if annotation_only_names:
            renpy_type_checking_imports.append((typ, mod, tuple(annotation_only_names)))

    lines = merged_source.splitlines(keepends=True)

    # If nothing to move to TYPE_CHECKING, just write the updated __future__ and return
    if not renpy_type_checking_imports:
        try:
            with open(file_path, "w", encoding="utf-8", newline="") as f:
                f.writelines(lines)
        except IOError as e:
            print(f"[WARNING] Could not write file {file_path}: {e}", file=sys.stderr)
        return

        # Find the lines to remove/modify (the new renpy imports at the top level)
    # Handles name-level splitting: removes annotation-only names from the import line,
    # keeping runtime names at the top level.
    lines_to_remove: set[int] = set()
    modified_lines: dict[int, str] = {}

    for i, line in enumerate(lines):
        stripped = line.strip()
        for typ, mod, names in renpy_type_checking_imports:
            if typ == "from" and stripped.startswith(f"from {mod} import"):
                import_names = [n.strip() for n in stripped[len(f"from {mod} import ") :].rstrip().split(",")]
                import_names = [n.split(" as ")[0].split(" as")[0].strip() for n in import_names]
                if sorted(import_names) == sorted(names):
                    lines_to_remove.add(i)
                    break
                elif all(n in import_names for n in names):
                    # Partial match: remove only the annotation-only names from the line
                    remaining = [n for n in import_names if n not in names]
                    if remaining:
                        joiner = ", "
                        new_line = "from " + mod + " import " + joiner.join(remaining)
                        if not new_line.endswith(eol):
                            new_line += eol
                        modified_lines[i] = new_line
                    else:
                        lines_to_remove.add(i)
                    break
            elif typ == "import" and stripped == f"import {mod}":
                lines_to_remove.add(i)
                break
            elif typ == "import" and stripped == f"import {mod}":
                lines_to_remove.add(i)
                break

    # Build new lines without the removed imports and Protocol classes
    # Modified lines (from name-level splitting) are used instead of originals.
    new_lines: list[str] = []
    for i, line in enumerate(lines):
        if i in modified_lines:
            new_lines.append(modified_lines[i])
        elif i not in lines_to_remove:
            new_lines.append(line)

    # Find where to insert the TYPE_CHECKING block
    import_start_line: int | None = None
    paren_depth = 0
    insert_at = 0
    for i, line in enumerate(new_lines):
        stripped = line.strip()

        if import_start_line is not None:
            paren_depth += stripped.count("(") - stripped.count(")")
            if paren_depth <= 0:
                import_start_line = None
                insert_at = i + 1
                continue
            else:
                continue

        if not stripped or stripped.startswith("#") or stripped.startswith('"') or stripped.startswith("'"):
            insert_at = i + 1
            continue
        if stripped.startswith("import ") or stripped.startswith("from "):
            insert_at = i + 1
            open_parens = stripped.count("(")
            close_parens = stripped.count(")")
            if open_parens > close_parens:
                import_start_line = i
                paren_depth = open_parens - close_parens
            continue
        if stripped.startswith("if TYPE_CHECKING"):
            for j in range(i, len(new_lines)):
                if new_lines[j].strip() == "":
                    for k in range(j + 1, len(new_lines)):
                        if new_lines[k].strip():
                            if not new_lines[k].startswith(("    ", "\t")):
                                insert_at = k
                                break
                            else:
                                break
                        break
                    if insert_at > i:
                        break
                    insert_at = j + 1
                elif new_lines[j].strip().startswith("if ") and j > i:
                    insert_at = j
                    break
            if insert_at > i:
                break
            insert_at = i + 1
            break
        break

    has_type_checking_block = any(line.strip().startswith("if TYPE_CHECKING") for line in new_lines)

    # Build the TYPE_CHECKING block content
    type_checking_lines: list[str] = []
    if not has_type_checking_block:
        type_checking_lines.append(f"if TYPE_CHECKING:{eol}")

    for typ, mod, names in renpy_type_checking_imports:
        if typ == "import":
            type_checking_lines.append(f"    import {mod}{eol}")
        elif typ == "from":
            name_str = ", ".join(names)
            type_checking_lines.append(f"    from {mod} import {name_str}{eol}")

    if not has_type_checking_block:
        type_checking_lines.append(eol)

    # Insert the TYPE_CHECKING block
    new_lines[insert_at:insert_at] = type_checking_lines

    # Add TYPE_CHECKING to from typing import if needed
    has_type_checking_import = any(
        "TYPE_CHECKING" in names for (t, m, names) in merged_imports if m == "typing" or m == "typing_extensions"
    )

    if not has_type_checking_import:
        # Find the typing import line and add TYPE_CHECKING, or add a new one
        found_typing_line = False
        for i, line in enumerate(new_lines):
            stripped = line.strip()
            if stripped.startswith("from typing import"):
                found_typing_line = True
                if "TYPE_CHECKING" not in stripped:
                    if stripped.endswith("\n"):
                        new_lines[i] = stripped.rstrip("\n") + ", TYPE_CHECKING" + eol
                    else:
                        new_lines[i] = stripped + ", TYPE_CHECKING" + eol
                    has_type_checking_import = True
                break
        if not found_typing_line:
            # No typing import exists - add one before the TYPE_CHECKING block
            tc_block_start = None
            for i, line in enumerate(new_lines):
                if line.strip().startswith("if TYPE_CHECKING"):
                    tc_block_start = i
                    break
            if tc_block_start is not None:
                new_lines.insert(tc_block_start, f"from typing import TYPE_CHECKING{eol}")
                has_type_checking_import = True

    if lines_to_remove:
        msg_parts = [f"{m}" for (t, m, n) in renpy_type_checking_imports]
        # print(f"  Moved to TYPE_CHECKING: {', '.join(msg_parts)}", file=sys.stderr)

    # Handle the `type_check_only` import: `typing.type_check_only` only exists in
    # Python 3.14+, so a top-level `from typing import ..., type_check_only` would
    # fail on Ren'Py's Python 3.12 at runtime. Since `@type_check_only` decorators
    # are only used inside the TYPE_CHECKING block (on Protocol classes moved there),
    # move `type_check_only` from the top-level typing import into the TYPE_CHECKING
    # block where it is never evaluated at runtime.
    _fix_type_check_only_import(new_lines, has_type_checking_block, eol)

    try:
        with open(file_path, "w", encoding="utf-8", newline="") as f:
            f.writelines(new_lines)
    except IOError as e:
        print(f"[WARNING] Could not write TYPE_CHECKING block to {file_path}: {e}", file=sys.stderr)


def _restore_type_parameters(source_pyi: Path, target_py: Path) -> None:
    """
    Restore PEP 695 generic type parameters (e.g. `[T]`) from the pyi stub
    into the merged py file. The ApplyTypeAnnotationsVisitor from libcst
    drops `type_parameters` on FunctionDef because it only stores
    `parameters` and `returns` in FunctionAnnotation.
    """
    try:
        import libcst as cst
    except ImportError:
        return  # libcst not available, skip

    # Read the pyi stub
    try:
        pyi_source = source_pyi.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return

    # Read the merged py file
    try:
        py_source = target_py.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return

    # Parse pyi to find functions with type_parameters
    try:
        pyi_cst = cst.parse_module(pyi_source)
    except Exception:
        return

    # Collect type_parameters from pyi functions
    pyi_type_params = {}
    for node in pyi_cst.body:
        if isinstance(node, cst.FunctionDef) and node.type_parameters is not None:
            pyi_type_params[node.name.value] = node.type_parameters

    if not pyi_type_params:
        return  # No generic functions in the stub

    # Parse the merged py file
    try:
        py_cst = cst.parse_module(py_source)
    except Exception:
        return

    # Create a transformer that injects type_parameters
    class _TypeParameterInjector(cst.CSTTransformer):
        def __init__(self, type_params_map):
            self.type_params_map = type_params_map

        def leave_FunctionDef(self, original, updated):
            if original.name.value in self.type_params_map:
                tp = self.type_params_map[original.name.value]
                return updated.with_changes(type_parameters=tp)
            return updated

    # Apply the transformer
    transformer = _TypeParameterInjector(pyi_type_params)
    result_cst = py_cst.visit(transformer)
    result_code = result_cst.code

    # Write the result back
    try:
        target_py.write_text(result_code, encoding="utf-8")
    except IOError as e:
        print(f"[WARNING] Could not write type parameters to {target_py}: {e}", file=sys.stderr)


def fix_missing_imports(file_path: Path) -> None:
    """
    Adds missing module imports (e.g. `import typing`) when the merged code
    uses `typing.X` but only had `from typing import ...` in the original.
    Only adds imports at the top level, before any statements.
    """
    try:
        with open(file_path, "r", encoding="utf-8", errors="replace", newline="") as f:
            source = f.read()
    except (UnicodeDecodeError, IOError) as e:
        print(f"[WARNING] Could not read {file_path} for import fixing: {e}", file=sys.stderr)
        return

    # Detect line ending style
    if "\r\n" in source:
        eol = "\r\n"
    else:
        eol = "\n"

    try:
        tree = ast.parse(source)
    except SyntaxError:
        return

    imported_names: Set[str] = set()
    imported_as_module: Set[str] = set()

    for node in tree.body:
        if isinstance(
            node,
            (
                ast.FunctionDef,
                ast.AsyncFunctionDef,
                ast.ClassDef,
                ast.Assign,
                ast.AnnAssign,
                ast.AugAssign,
                ast.Expr,
                ast.If,
                ast.For,
                ast.While,
                ast.With,
                ast.Try,
                ast.Raise,
                ast.Return,
            ),
        ):
            break
        if isinstance(node, ast.Import):
            for alias in node.names:
                mod = alias.name.split(".")[0]
                imported_as_module.add(mod)
                imported_names.add(alias.asname or mod)
        elif isinstance(node, ast.ImportFrom):
            for alias in node.names:
                imported_names.add(alias.asname or alias.name)

    used_modules: Set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Attribute) and isinstance(node.value, ast.Name):
            name = node.value.id
            if name.islower() and name not in imported_names:
                used_modules.add(name)

    missing = used_modules - imported_as_module
    if not missing:
        return

    lines = source.splitlines(keepends=True)
    insert_at = 0
    while insert_at < len(lines):
        stripped = lines[insert_at].lstrip()
        if stripped.startswith("#"):
            insert_at += 1
            continue
        break

    if insert_at < len(lines) and (
        lines[insert_at].lstrip().startswith('"""') or lines[insert_at].lstrip().startswith("'''")
    ):
        quote = lines[insert_at].lstrip()[:3]
        for i in range(insert_at, len(lines)):
            if lines[i].count(quote) >= 2 or (i > insert_at and quote in lines[i]):
                insert_at = i + 1
                break

    new_imports = [f"import {m}{eol}" for m in sorted(missing)]
    lines[insert_at:insert_at] = new_imports
    if insert_at > 0 and not lines[insert_at - 1].endswith(eol * 2):
        lines.insert(insert_at, eol)

    try:
        with open(file_path, "w", encoding="utf-8", newline="") as f:
            f.writelines(lines)
    except IOError as e:
        print(f"[WARNING] Could not write imports to {file_path}: {e}", file=sys.stderr)


def _normalize_line_endings(file_path: Path) -> None:
    """
    Normalize file to LF line endings. This prevents git from seeing
    full-file churn when pytype merge writes CRLF on Windows.
    """
    try:
        with open(file_path, "rb") as f:
            content = f.read()
    except IOError as e:
        print(f"[WARNING] Could not read {file_path} for line ending fix: {e}", file=sys.stderr)
        return

    if b"\r\n" not in content:
        return  # Already LF

    content = content.replace(b"\r\n", b"\n")
    try:
        with open(file_path, "wb") as f:
            f.write(content)
    except IOError as e:
        print(f"[WARNING] Could not write {file_path} for line ending fix: {e}", file=sys.stderr)


def _has_future_import(source: str) -> bool:
    """Check if the source has a `from __future__ import ...` statement."""
    return "__future__" in source and re.search(r"^\s*from\s+__future__\s+import", source, re.MULTILINE)


def _fix_future_imports(file_path: Path, original_source: str) -> None:
    """
    Ensure that `from __future__ import ...` lines are at the very top of the file
    (after comments/docstring) if the original file had them.
    The merge tool may insert new imports before the __future__ line, which causes
    a SyntaxError at runtime.
    """
    if not _has_future_import(original_source):
        return

    try:
        with open(file_path, "r", encoding="utf-8", errors="replace", newline="") as f:
            merged_source = f.read()
    except (UnicodeDecodeError, IOError) as e:
        print(f"[WARNING] Could not read {file_path} for __future__ fix: {e}", file=sys.stderr)
        return

    # Detect line ending style
    if "\r\n" in merged_source:
        eol = "\r\n"
    else:
        eol = "\n"

    lines = merged_source.splitlines(keepends=True)

    # Find all __future__ import lines
    future_lines = []
    non_future_lines = []
    future_indices = set()

    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith("from __future__ import") or stripped.startswith("from __future__ import ("):
            future_lines.append(line)
            future_indices.add(i)
        else:
            non_future_lines.append((i, line))

    if not future_lines:
        return

    # Check if the first __future__ line is already before any non-comment, non-__future__ statement
    first_statement = None
    for i, line in enumerate(lines):
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if stripped.startswith('"') or stripped.startswith("'"):
            # Docstring - skip it
            continue
        if stripped in future_indices:
            break
        if first_statement is None:
            first_statement = i

    if first_statement is None:
        # __future__ is already first - no change needed
        return

    # Rebuild: comments/docstring from the top, then __future__ lines, then everything else
    header_lines = []
    body_lines = []
    past_header = False

    for i, line in enumerate(lines):
        if i in future_indices:
            continue
        stripped = line.strip()
        if not past_header:
            if not stripped or stripped.startswith("#") or stripped.startswith('"') or stripped.startswith("'"):
                header_lines.append(line)
                continue
            else:
                past_header = True
        body_lines.append(line)

    # Rebuild with __future__ lines right after the header
    new_lines = header_lines + future_lines
    if body_lines and not body_lines[0].startswith("\n") and not body_lines[0].startswith(eol):
        new_lines.append(eol)
    new_lines.extend(body_lines)

    # print(f"  Fixed __future__ import ordering", file=sys.stderr)

    try:
        with open(file_path, "w", encoding="utf-8", newline="") as f:
            f.writelines(new_lines)
    except IOError as e:
        print(f"[WARNING] Could not write {file_path} for __future__ fix: {e}", file=sys.stderr)


def _verify_merge(file_path: Path, original_source: str) -> bool:
    """
    Verify the merged file is syntactically valid using ast.parse.
    If the original file had `from __future__ import ...`, verify it's still at the top.
    If verification fails, restore the original from git.
    Returns True if the merge is valid, False if it was restored.
    """
    try:
        with open(file_path, "r", encoding="utf-8", errors="replace", newline="") as f:
            merged_source = f.read()
    except (UnicodeDecodeError, IOError) as e:
        print(f"  [VERIFY] Could not read merged file: {e}", file=sys.stderr)
        return _restore_from_git(file_path)

    # Check 1: Syntax validity
    try:
        ast.parse(merged_source)
    except SyntaxError as e:
        print(f"  [VERIFY] Syntax error in merged file: {e}", file=sys.stderr)
        if e.lineno:
            print("\n".join(merged_source.split("\n")[e.lineno - 10 : e.lineno + 10]))
        return _restore_from_git(file_path)

    # Check 2: __future__ import ordering (if original had them)
    if _has_future_import(original_source):
        lines = merged_source.splitlines()
        future_seen = False
        non_future_non_comment_seen = False
        for line in lines:
            stripped = line.strip()
            if not stripped or stripped.startswith("#") or stripped.startswith('"') or stripped.startswith("'"):
                continue
            if stripped.startswith("from __future__ import"):
                if non_future_non_comment_seen:
                    print(f"  [VERIFY] __future__ import after other statements", file=sys.stderr)
                    return _restore_from_git(file_path)
                future_seen = True
            else:
                if not future_seen:
                    non_future_non_comment_seen = True

    # Check 3: Check for undefined TypeVars in annotations
    # Scan for patterns like `Callable[P, R]` or `Callable[[T], U]` where
    # the TypeVar names might not be defined
    annotation_tvars = set()
    for match in re.finditer(r"Callable\[([^\[\]]+)\]", merged_source):
        args = match.group(1)
        # Check for single letter TypeVars in annotations
        for part in args.split(","):
            part = part.strip()
            if part.isidentifier() and part[0].isupper() and len(part) <= 2:
                annotation_tvars.add(part)

    if annotation_tvars:
        # Check if these are defined as TypeVars or are imported types
        try:
            tree = ast.parse(merged_source)
        except SyntaxError:
            return _restore_from_git(file_path)

        defined_names: Set[str] = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                defined_names.add(node.name)
            elif isinstance(node, ast.FunctionDef):
                defined_names.add(node.name)
            elif isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        defined_names.add(target.id)

        # Also check imports
        imported_names: Set[str] = set()
        for node in tree.body:
            if isinstance(node, ast.Import):
                for alias in node.names:
                    imported_names.add(alias.asname or alias.name.split(".")[0])
            elif isinstance(node, ast.ImportFrom):
                if node.module:
                    imported_names.add(node.module.split(".")[0])
                for alias in node.names:
                    imported_names.add(alias.asname or alias.name)

        undefined = annotation_tvars - defined_names - imported_names - {"True", "False", "None"}
        if undefined:
            print(f"  [VERIFY] Undefined annotation TypeVars: {', '.join(sorted(undefined))}", file=sys.stderr)
            return _restore_from_git(file_path)

    return True


def _restore_from_git(file_path: Path) -> bool:
    """Restore a file from git. Returns False (merge failed)."""
    try:
        file_path = file_path.resolve()
        subprocess.run(
            ["git", "checkout", "--", str(file_path)],
            cwd=file_path.parent,
            capture_output=True,
            timeout=30,
        )
        print(f"  Restored from git: {file_path.name}", file=sys.stderr)
    except Exception as e:
        print(f"  [ERROR] Could not restore from git: {e}", file=sys.stderr)
    return False


def process_merge(source_pyi: Path, target_py: Path) -> bool:
    """
    Merge type annotations from a .pyi stub into a .py source file.
    Returns True if the merge was successful, False if it was restored.
    """
    try:
        try:
            with open(target_py, "r", encoding="utf-8", errors="replace", newline="") as f:
                original_source = f.read()
        except Exception:
            original_source = ""

        # Step 1: Clean bare type comments
        clean_type_comments(target_py)

        # Step 2: Run pytype merge
        merge_files(pyi_path=str(source_pyi), py_path=str(target_py), mode=Mode.OVERWRITE)

        # Step 3: Fix missing module imports (e.g. `import typing`)
        fix_missing_imports(target_py)

        # Step 4: Fix missing typing annotation imports (e.g. `Self`)
        _fix_typing_annotation_imports(target_py)

        # Step 5: Remove polluted import pollution (variable names merged as imports)
        if original_source:
            _restore_original_imports(target_py, original_source)

        # Step 6: Move new renpy-internal imports to TYPE_CHECKING block
        if original_source:
            _move_type_checking_imports(target_py, original_source)

        # Step 6b: Add type-only definitions from stub's TYPE_CHECKING blocks
        _add_type_checking_definitions(target_py, source_pyi)

        # Step 6c: Restore PEP 695 generic type parameters [T] lost during merge
        _restore_type_parameters(source_pyi, target_py)

        # Step 7: Fix __future__ import ordering
        if original_source:
            _fix_future_imports(target_py, original_source)

        # Step 8: Normalize line endings to LF
        _normalize_line_endings(target_py)

        # Step 9: Verify the merged file
        if original_source:
            if not _verify_merge(target_py, original_source):
                return False

        return True
    except SyntaxError as e:
        print(f"[ERROR] Syntax error merging {source_pyi} -> {target_py}: {e}", file=sys.stderr)
        _restore_from_git(target_py)
        return False
    except Exception as e:
        print(f"[ERROR] merging {source_pyi} -> {target_py}: {e}", file=sys.stderr)
        traceback.print_exc()
        return False


def main():
    import argparse

    ap = argparse.ArgumentParser()
    ap.add_argument(
        "filters", nargs="*", type=str, help="File filters that select what to merge. Leave blank to merge everything."
    )
    args = ap.parse_args()

    file_filters: list[str] = args.filters

    source_files = collect_source_files(config.pyi_path)
    if file_filters:
        temp = source_files
        source_files = set()

        for sf in temp:
            for ffilter in file_filters:
                if ffilter in str(sf):
                    source_files.add(sf)
                    break
        source_files = list(source_files)

    success_count = 0
    skip_count = 0
    fail_count = 0
    restored_count = 0

    for source_pyi in source_files:
        target_py = resolve_target_path(source_pyi, config.pyi_path, config.renpy_path)

        if not target_py:
            rel_path = source_pyi.relative_to(config.pyi_path)
            print(f"[SKIP] No matching .py or .pyi file: {rel_path}", file=sys.stderr)
            skip_count += 1
            continue

        try:
            rel_target = target_py.relative_to(config.renpy_path).as_posix()
        except ValueError:
            rel_target = target_py.name

        if target_py.name == "__init__.py":
            print(f"[SKIP] __init__.py: {rel_target}", file=sys.stderr)
            skip_count += 1
            continue

        if any(rel_target == f or rel_target.startswith(f.rstrip("/") + "/") for f in config.exclude_files):
            print(f"[SKIP] Excluded: {rel_target}", file=sys.stderr)
            skip_count += 1
            continue

        display_name = target_py.relative_to(config.renpy_path)
        print(f"[PROCESS] {display_name}")

        if process_merge(source_pyi.resolve(), target_py.resolve()):
            success_count += 1
        else:
            restored_count += 1
            fail_count += 1

    print(f"\nMerge summary:", file=sys.stderr)
    print(f"  Success: {success_count}", file=sys.stderr)
    print(f"  Skipped: {skip_count}", file=sys.stderr)
    print(f"  Restored (failed verification): {restored_count}", file=sys.stderr)


if __name__ == "__main__":
    main()
