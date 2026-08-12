"""
scripts/cherrypick_pyi.py - Per-parameter cherrypick merge of .pyi stub files.

Merges a generated .pyi file (from stubgen) into a current .pyi file,
preserving current quality while cherrypicking better type annotations
from the generated version at the per-parameter granularity.

Annotation quality ladder (used for cherrypicking):
    0 = None (no annotation)
    1 = Incomplete (stubgen couldn't infer)
    2 = Any (generic fallback)
    3 = specific type (e.g., float, list[str], Callable)

For each parameter/attribute:
    If gen_rank > curr_rank, take gen's annotation (fills in missing/new types)
    If gen_rank <= curr_rank, keep curr's annotation (protects from destructive edits)
"""

import ast
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Optional


# ## Annotation quality ######################################################


def annotation_rank(node: Optional[ast.AST]) -> int:
    """Rank annotation quality: 0=none, 1=Incomplete, 2=Any, 3=specific."""
    if node is None:
        return 0
    if isinstance(node, ast.Name):
        if node.id == "Incomplete":
            return 1
        if node.id == "Any":
            return 2
    return 3


def is_degenerate(node: Optional[ast.AST]) -> bool:
    """True if annotation is None, Incomplete, or bare Any."""
    return annotation_rank(node) < 3


# ## Byte offset helpers #####################################################


def _byte_offset(text: str, lineno: int, col_offset: int) -> int:
    """Convert (1-based line, 0-based col) to byte offset in text."""
    lines = text.splitlines(keepends=True)
    offset = 0
    for i in range(lineno - 1):
        if i < len(lines):
            offset += len(lines[i])
    return offset + col_offset


def _annotation_span(text: str, node: ast.AST) -> tuple[int, int]:
    """Get (start, end) byte offsets for an annotation AST node."""
    start = _byte_offset(text, node.lineno, node.col_offset)
    end = _byte_offset(text, node.end_lineno, node.end_col_offset)
    return (start, end)


def _get_source_segment(text: str, node: ast.AST) -> str:
    """Get the verbatim source text of an AST node."""
    start, end = _annotation_span(text, node)
    return text[start:end]


def _get_source_lines(text: str, start_line: int, end_line: int, start_col: int = 0, end_col: int = 0) -> str:
    """Get source text spanning from start_line:start_col to end_line:end_col."""
    start = _byte_offset(text, start_line, start_col)
    end = _byte_offset(text, end_line, end_col)
    return text[start:end]


@dataclass
class Replacement:
    """A surgical text replacement in the current source."""

    start: int  # byte offset, inclusive
    end: int  # byte offset, exclusive
    text: str  # replacement text


def apply_replacements(text: str, replacements: list[Replacement]) -> str:
    """Apply replacements in reverse order (by start offset descending)."""
    result = text
    for r in sorted(replacements, key=lambda x: x.start, reverse=True):
        result = result[: r.start] + r.text + result[r.end :]
    return result


# ## Symbol indexing and matching ############################################


def _param_count(func_node: ast.AST) -> int:
    """Count positional-or-keyword parameters (excluding self/cls)."""
    if not isinstance(func_node, (ast.FunctionDef, ast.AsyncFunctionDef)):
        return 0
    return len(func_node.args.args) + len(func_node.args.posonlyargs)


def _build_symbol_index(tree: ast.AST) -> dict[str, list[ast.AST]]:
    """Build a name -> list-of-defs map from an AST.

    Handles overloaded functions (multiple defs with the same name).
    """
    index: dict[str, list[ast.AST]] = {}
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            index.setdefault(node.name, []).append(node)
        elif isinstance(node, ast.ClassDef):
            index.setdefault(node.name, []).append(node)
        elif isinstance(node, ast.TypeAlias):
            index.setdefault(node.name.id, []).append(node)
        elif isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
            index.setdefault(node.target.id, []).append(node)
    return index


def _match_def(curr_def: ast.AST, gen_candidates: list[ast.AST]) -> Optional[ast.AST]:
    """Match a curr definition to the best gen candidate by signature shape.

    For functions: match by name + parameter count (handles overloads).
    For classes/type-aliases: match by name.
    """
    if not gen_candidates:
        return None

    if isinstance(curr_def, (ast.FunctionDef, ast.AsyncFunctionDef)):
        curr_count = _param_count(curr_def)
        # Exact match by param count
        for gen_def in gen_candidates:
            if isinstance(gen_def, (ast.FunctionDef, ast.AsyncFunctionDef)):
                if _param_count(gen_def) == curr_count:
                    return gen_def
        # No exact match, closest param count
        return min(
            (g for g in gen_candidates if isinstance(g, (ast.FunctionDef, ast.AsyncFunctionDef))),
            key=lambda g: abs(_param_count(g) - curr_count),
            default=None,
        )

    if isinstance(curr_def, ast.ClassDef):
        for gen_def in gen_candidates:
            if isinstance(gen_def, ast.ClassDef):
                return gen_def
        return None

    if isinstance(curr_def, ast.TypeAlias):
        for gen_def in gen_candidates:
            if isinstance(gen_def, ast.TypeAlias):
                return gen_def
        return None

    if isinstance(curr_def, ast.AnnAssign):
        for gen_def in gen_candidates:
            if isinstance(gen_def, ast.AnnAssign):
                return gen_def
        return None

    return None


def _find_param(params: list[ast.arg], name: str) -> Optional[ast.arg]:
    """Find a parameter by name in a list of ast.arg nodes."""
    for p in params:
        if p.arg == name:
            return p
    return None


def _collect_all_params(func_node: ast.FunctionDef | ast.AsyncFunctionDef) -> list[ast.arg]:
    """Collect all parameters in order: posonlyargs, args, kwonlyargs."""
    params = []
    params.extend(func_node.args.posonlyargs)
    params.extend(func_node.args.args)
    params.extend(func_node.args.kwonlyargs)
    return params


# ## Function annotation cherrypicking #######################################


def _find_closing_paren(text: str, func_node: ast.FunctionDef | ast.AsyncFunctionDef) -> int:
    """Find byte offset of the closing ')' in the function signature."""
    sig_start = _byte_offset(text, func_node.lineno, func_node.col_offset)
    sig_end = _byte_offset(text, func_node.end_lineno, func_node.end_col_offset)
    sig_text = text[sig_start:sig_end]

    paren_count = 0
    for i, ch in enumerate(sig_text):
        if ch == "(":
            paren_count += 1
        elif ch == ")":
            paren_count -= 1
            if paren_count == 0:
                return sig_start + i
    return sig_start + len(sig_text)  # fallback


def _gen_param_text(gen_text: str, gen_param: ast.arg) -> str:
    """Get the text of a parameter including its annotation (no default)."""
    if gen_param.annotation:
        return f"{gen_param.arg}: {_get_source_segment(gen_text, gen_param.annotation)}"
    return gen_param.arg


def cherrypick_function_params(
    curr_def: ast.FunctionDef | ast.AsyncFunctionDef,
    gen_def: ast.FunctionDef | ast.AsyncFunctionDef,
    curr_text: str,
    gen_text: str,
) -> list[Replacement]:
    """Generate replacements for function parameter and return type annotations.

    Per-parameter cherrypicking:
    - If gen has a better annotation (higher rank), take gen's
    - If curr has a better or equal annotation, keep curr's
    - If gen has a new parameter that curr lacks, add it
    """
    replacements: list[Replacement] = []

    curr_params = _collect_all_params(curr_def)
    gen_params = _collect_all_params(gen_def)
    curr_param_names = {p.arg for p in curr_params}

    # ## Per-parameter cherrypick ########################################
    for curr_param in curr_params:
        gen_param = _find_param(gen_params, curr_param.arg)
        if gen_param is None:
            continue

        curr_ann = curr_param.annotation
        gen_ann = gen_param.annotation

        curr_rank = annotation_rank(curr_ann)
        gen_rank = annotation_rank(gen_ann)

        if gen_rank > curr_rank:
            # Gen has better annotation — take it
            if curr_ann is not None:
                # Replace existing annotation text
                start, end = _annotation_span(curr_text, curr_ann)
                new_text = _get_source_segment(gen_text, gen_ann)
                replacements.append(Replacement(start, end, new_text))
            else:
                # curr had no annotation — insert `: Type` after param name
                param_name_end = _byte_offset(curr_text, curr_param.end_lineno, curr_param.end_col_offset)
                new_text = f": {_get_source_segment(gen_text, gen_ann)}"
                replacements.append(Replacement(param_name_end, param_name_end, new_text))

    # ## New parameters in gen that don't exist in curr ##################
    for gen_param in gen_params:
        if gen_param.arg in curr_param_names:
            continue
        # Skip self/cls
        if gen_param.arg in ("self", "cls"):
            continue

        # Insert new parameter before the closing paren
        closing_paren = _find_closing_paren(curr_text, curr_def)
        param_text = _gen_param_text(gen_text, gen_param)
        replacements.append(Replacement(closing_paren, closing_paren, f", {param_text}"))

    # ## Return type cherrypick ##########################################
    curr_ret = curr_def.returns
    gen_ret = gen_def.returns

    curr_ret_rank = annotation_rank(curr_ret)
    gen_ret_rank = annotation_rank(gen_ret)

    if gen_ret_rank > curr_ret_rank:
        if curr_ret is not None:
            # Replace existing return annotation
            start, end = _annotation_span(curr_text, curr_ret)
            new_text = _get_source_segment(gen_text, gen_ret)
            replacements.append(Replacement(start, end, new_text))
        elif gen_ret is not None:
            # curr had no return annotation, gen has one — insert `-> Type`
            closing_paren = _find_closing_paren(curr_text, curr_def)
            new_text = f" -> {_get_source_segment(gen_text, gen_ret)}"
            replacements.append(Replacement(closing_paren + 1, closing_paren + 1, new_text))

    return replacements


# ## Class attribute cherrypicking ###########################################


def cherrypick_class_attrs(
    curr_class: ast.ClassDef,
    gen_class: ast.ClassDef,
    curr_text: str,
    gen_text: str,
) -> list[Replacement]:
    """Generate replacements for class attribute annotations.

    Cherrypicks per-attribute. Also handles adding new attributes from gen.
    """
    replacements: list[Replacement] = []

    # Index curr and gen attributes by name
    curr_attrs: dict[str, ast.AnnAssign] = {}
    for node in curr_class.body:
        if isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
            curr_attrs[node.target.id] = node

    gen_attrs: dict[str, ast.AnnAssign] = {}
    for node in gen_class.body:
        if isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
            gen_attrs[node.target.id] = node

    # ## Cherrypick existing attributes ##################################
    for name, curr_aa in curr_attrs.items():
        if name not in gen_attrs:
            continue
        gen_aa = gen_attrs[name]

        curr_ann = curr_aa.annotation
        gen_ann = gen_aa.annotation

        curr_rank = annotation_rank(curr_ann)
        gen_rank = annotation_rank(gen_ann)

        if gen_rank > curr_rank:
            start, end = _annotation_span(curr_text, curr_ann)
            new_text = _get_source_segment(gen_text, gen_ann)
            replacements.append(Replacement(start, end, new_text))

    # ## New attributes from gen not in curr #############################
    # Find insertion point: after the last attribute, before the first method
    last_attr_line = 0
    first_method_line: Optional[int] = None
    for node in curr_class.body:
        if isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
            last_attr_line = max(last_attr_line, node.end_lineno)
        elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            if first_method_line is None or node.lineno < first_method_line:
                first_method_line = node.lineno

    for name, gen_aa in gen_attrs.items():
        if name in curr_attrs:
            continue
        # Only add non-degenerate attributes
        if is_degenerate(gen_aa.annotation):
            continue

        if first_method_line is not None:
            insert_pos = _byte_offset(curr_text, first_method_line, 0)
        else:
            # After the last attribute (or at end of class body)
            lines = curr_text.splitlines(keepends=True)
            if last_attr_line > 0 and last_attr_line - 1 < len(lines):
                insert_pos = _byte_offset(curr_text, last_attr_line, 0) + len(lines[last_attr_line - 1])
            else:
                # At end of class body
                insert_pos = _byte_offset(curr_text, curr_class.end_lineno, curr_class.end_col_offset) - 1

        gen_ann_text = _get_source_segment(gen_text, gen_aa.annotation)
        new_text = f"    {name}: {gen_ann_text}\n"
        replacements.append(Replacement(insert_pos, insert_pos, new_text))

    return replacements


# ## TYPE_CHECKING block merging #############################################


def _collect_type_checking_defs(tree: ast.AST) -> dict[str, list[ast.stmt]]:
    """Collect all named definitions inside `if TYPE_CHECKING:` blocks."""
    defs: dict[str, list[ast.stmt]] = {}
    for node in tree.body:
        if isinstance(node, ast.If) and isinstance(node.test, ast.Name) and node.test.id == "TYPE_CHECKING":
            for item in node.body:
                if isinstance(item, ast.ClassDef):
                    defs[item.name] = [item]
                elif isinstance(item, ast.TypeAlias):
                    defs[item.name.id] = [item]
                elif isinstance(item, ast.FunctionDef):
                    defs[item.name] = [item]
                elif isinstance(item, ast.AnnAssign) and isinstance(item.target, ast.Name):
                    defs[item.target.id] = [item]
                elif isinstance(item, (ast.ImportFrom, ast.Import)):
                    for alias in item.names:
                        alias_name = alias.asname or alias.name
                        if alias_name not in defs:
                            defs[alias_name] = []
                        defs[alias_name].append(item)
    return defs


def _get_top_level_names(tree: ast.AST) -> set[str]:
    """Get names of all top-level definitions in the module."""
    names: set[str] = set()
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            names.add(node.name)
        elif isinstance(node, ast.TypeAlias):
            names.add(node.name.id)
        elif isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
            names.add(node.target.id)
    return names


def merge_type_checking(
    curr_text: str,
    curr_tree: ast.AST,
    gen_text: str,
    gen_tree: ast.AST,
) -> str:
    """Merge TYPE_CHECKING definitions from generated file into current file.

    - Preserves all current TYPE_CHECKING definitions
    - Adds new definitions from gen that don't exist in curr (top-level or TYPE_CHECKING)
    """
    # Collect all names already defined in curr (top-level + TYPE_CHECKING)
    curr_top_names = _get_top_level_names(curr_tree)
    curr_tc_defs = _collect_type_checking_defs(curr_tree)
    curr_all_names = curr_top_names | set(curr_tc_defs.keys())

    # Get gen's TYPE_CHECKING definitions
    gen_tc_defs = _collect_type_checking_defs(gen_tree)

    # Find new definitions in gen's TYPE_CHECKING that aren't in curr
    new_def_sources: list[str] = []
    for name, items in gen_tc_defs.items():
        if name in curr_all_names:
            continue
        for item in items:
            if isinstance(item, (ast.ImportFrom, ast.Import)):
                src = _get_source_segment(gen_text, item)
                if src not in new_def_sources:
                    new_def_sources.append(src)
            else:
                # Get the full definition including decorators
                lines = gen_text.splitlines()
                start_line = item.lineno - 1
                while start_line > 0:
                    if lines[start_line - 1].strip().startswith("@"):
                        start_line -= 1
                    else:
                        break
                start = _byte_offset(gen_text, start_line + 1, 0)
                end = _byte_offset(gen_text, item.end_lineno, item.end_col_offset)
                src = gen_text[start:end]
                if src not in new_def_sources:
                    new_def_sources.append(src)

    if not new_def_sources:
        return curr_text

    # Detect line ending style
    eol = "\r\n" if "\r\n" in curr_text else "\n"

    lines = curr_text.splitlines(keepends=True)

    # Find existing TYPE_CHECKING block
    tc_start = None
    tc_end = None
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith("if TYPE_CHECKING"):
            tc_start = i
            # Find where the block ends (first non-indented line after the block)
            for j in range(i + 1, len(lines)):
                inner = lines[j].strip()
                if not inner:
                    continue
                if inner.startswith(("    ", "\t")):
                    tc_end = j + 1  # still in the block
                else:
                    if tc_end is None or j > tc_end:
                        break
            if tc_end is None:
                tc_end = len(lines)
            break

    if tc_start is not None:
        # Insert new definitions at the end of the existing TYPE_CHECKING block
        # (after the last indented line, before the blank line / block end)
        insert_lines: list[str] = []
        for d in new_def_sources:
            # Check if this def is already in the block
            d_text = f"    {d}{eol}"
            already_present = False
            for k in range(tc_start + 1, tc_end):
                if lines[k].strip() == d.strip():
                    already_present = True
                    break
            if not already_present:
                insert_lines.append(d_text)
        if insert_lines:
            insert_lines.append(eol)
            lines[tc_end:tc_end] = insert_lines
    else:
        # No TYPE_CHECKING block — create one
        # Find insertion point: after all imports, before first definition
        insert_at = 0
        for i, line in enumerate(lines):
            stripped = line.strip()
            if not stripped or stripped.startswith("#") or stripped.startswith('"') or stripped.startswith("'"):
                insert_at = i + 1
                continue
            if stripped.startswith("import ") or stripped.startswith("from "):
                insert_at = i + 1
                continue
            break

        tc_block = [f"if TYPE_CHECKING:{eol}"]
        tc_block.append(f"    from typing import TYPE_CHECKING{eol}")
        for d in new_def_sources:
            tc_block.append(f"    {d}{eol}")
        tc_block.append(eol)
        lines[insert_at:insert_at] = tc_block

    return "".join(lines)


# ## New symbol collection ###################################################


def collect_new_symbols(
    gen_tree: ast.AST,
    curr_tree: ast.AST,
    gen_text: str,
) -> list[str]:
    """Collect new top-level symbols from gen that don't exist in curr.

    These are symbols present in the generated file but absent from the
    current file — new classes, functions, or type aliases added to
    the Ren'Py codebase.
    """
    curr_names = _get_top_level_names(curr_tree)
    curr_tc_defs = _collect_type_checking_defs(curr_tree)
    curr_all_names = curr_names | set(curr_tc_defs.keys())

    new_symbols: list[str] = []
    for node in gen_tree.body:
        # Skip TYPE_CHECKING blocks (handled separately)
        if isinstance(node, ast.If) and isinstance(node.test, ast.Name) and node.test.id == "TYPE_CHECKING":
            continue

        name = None
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            name = node.name
        elif isinstance(node, ast.TypeAlias):
            name = node.name.id
        elif isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
            name = node.target.id
        elif isinstance(node, (ast.ImportFrom, ast.Import)):
            continue  # Skip imports — curr file has its own

        if name is not None and name not in curr_all_names:
            # Get the full source text including decorators
            lines = gen_text.splitlines()
            start_line = node.lineno - 1
            while start_line > 0:
                if lines[start_line - 1].strip().startswith("@"):
                    start_line -= 1
                else:
                    break
            start = _byte_offset(gen_text, start_line + 1, 0)
            end = _byte_offset(gen_text, node.end_lineno, node.end_col_offset)
            src = gen_text[start:end]
            if src.strip():
                new_symbols.append(src)

    return new_symbols


# ## Main merge function #####################################################


def cherrypick_merge_file(curr_path: Path, gen_path: Path) -> str:
    """Merge a generated .pyi file into a current .pyi file.

    Returns the merged text. Falls back to the original file on parse errors.
    """
    curr_text = curr_path.read_text(encoding="utf-8")
    gen_text = gen_path.read_text(encoding="utf-8")

    # Parse both files
    try:
        curr_tree = ast.parse(curr_text)
    except SyntaxError as e:
        print(f"  [WARNING] Syntax error in current file {curr_path}: {e}", file=sys.stderr)
        print(f"  Falling back to generated file", file=sys.stderr)
        return gen_text

    try:
        gen_tree = ast.parse(gen_text)
    except SyntaxError as e:
        print(f"  [WARNING] Syntax error in generated file {gen_path}: {e}", file=sys.stderr)
        print(f"  Keeping current (no merge)", file=sys.stderr)
        return curr_text

    # Build symbol index of generated file
    gen_index = _build_symbol_index(gen_tree)

    # Collect all replacements
    all_replacements: list[Replacement] = []

    # ## Walk curr tree and cherrypick ###################################
    for node in curr_tree.body:
        # Skip TYPE_CHECKING blocks — handled separately
        if isinstance(node, ast.If) and isinstance(node.test, ast.Name) and node.test.id == "TYPE_CHECKING":
            continue

        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            # Top-level function
            gen_candidates = gen_index.get(node.name, [])
            gen_def = _match_def(node, gen_candidates)
            if gen_def is not None and isinstance(gen_def, (ast.FunctionDef, ast.AsyncFunctionDef)):
                replacements = cherrypick_function_params(node, gen_def, curr_text, gen_text)
                all_replacements.extend(replacements)

        elif isinstance(node, ast.ClassDef):
            gen_candidates = gen_index.get(node.name, [])
            gen_class = _match_def(node, gen_candidates)
            if gen_class is not None and isinstance(gen_class, ast.ClassDef):
                # Cherrypick class attributes
                replacements = cherrypick_class_attrs(node, gen_class, curr_text, gen_text)
                all_replacements.extend(replacements)

                # Cherrypick class methods
                curr_methods: dict[str, list[ast.AST]] = {}
                for item in node.body:
                    if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
                        curr_methods.setdefault(item.name, []).append(item)

                gen_methods: dict[str, list[ast.AST]] = {}
                for item in gen_class.body:
                    if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
                        gen_methods.setdefault(item.name, []).append(item)

                for name, curr_candidates in curr_methods.items():
                    gen_cand = gen_methods.get(name, [])
                    for curr_method in curr_candidates:
                        gen_method = _match_def(curr_method, gen_cand)
                        if gen_method is not None and isinstance(gen_method, (ast.FunctionDef, ast.AsyncFunctionDef)):
                            replacements = cherrypick_function_params(curr_method, gen_method, curr_text, gen_text)
                            all_replacements.extend(replacements)

        elif isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
            # Module-level variable annotation
            gen_candidates = gen_index.get(node.target.id, [])
            for gen_node in gen_candidates:
                if isinstance(gen_node, ast.AnnAssign):
                    curr_ann = node.annotation
                    gen_ann = gen_node.annotation
                    curr_rank = annotation_rank(curr_ann)
                    gen_rank = annotation_rank(gen_ann)
                    if gen_rank > curr_rank:
                        start, end = _annotation_span(curr_text, curr_ann)
                        new_text = _get_source_segment(gen_text, gen_ann)
                        all_replacements.append(Replacement(start, end, new_text))
                    break

    # ## Apply replacements to curr text #################################
    merged_text = apply_replacements(curr_text, all_replacements)

    # Re-parse merged text for subsequent operations
    try:
        merged_tree = ast.parse(merged_text)
    except SyntaxError:
        print(f"  [WARNING] Merged file has syntax errors in {curr_path.name}, keeping current", file=sys.stderr)
        return curr_text

    # ## Merge TYPE_CHECKING blocks ######################################
    merged_text = merge_type_checking(merged_text, merged_tree, gen_text, gen_tree)

    # Re-parse for new symbol collection
    try:
        merged_tree = ast.parse(merged_text)
    except SyntaxError:
        return merged_text

    # ## Collect and append new symbols from gen #########################
    new_symbols = collect_new_symbols(gen_tree, merged_tree, gen_text)
    if new_symbols:
        # Ensure trailing newline
        if not merged_text.endswith("\n"):
            merged_text += "\n"
        if not merged_text.endswith("\n\n"):
            merged_text += "\n"
        merged_text += "\n\n".join(new_symbols) + "\n"

    return merged_text


# ## CLI for testing #########################################################


def main():
    """CLI: python -m scripts.cherrypick_pyi curr.pyi gen.pyi [output.pyi]"""
    import argparse

    ap = argparse.ArgumentParser(description="Cherrypick merge .pyi files")
    ap.add_argument("curr", type=Path, help="current .pyi file")
    ap.add_argument("gen", type=Path, help="Generated .pyi file")
    ap.add_argument("output", type=Path, nargs="?", help="Output file (default: stdout)")
    args = ap.parse_args()

    merged = cherrypick_merge_file(args.curr, args.gen)

    if args.output:
        args.output.write_text(merged, encoding="utf-8")
        print(f"Written to {args.output}", file=sys.stderr)
    else:
        print(merged, end="")


if __name__ == "__main__":
    main()
