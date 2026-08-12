"""
Extracts Python code from Ren'Py .rpy files and writes them to .py files.

Makes use of Ren'Py's internal parser to accurately extract code blocks.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.resolve()))
from config import config
sys.path.insert(0, str(config.renpy_path))

import renpy  # type: ignore

## Bootstrap
renpy.import_all()
renpy.importer.init_importer()

args = renpy.arguments.bootstrap()
renpy.game.args = args

# Load the script.
renpy.game.exception_info = "While loading the script."
renpy.game.script = renpy.script.Script()

############################################

from config import config

EARLY_PRIORITY: int = -99999999

type InitNodes = dict[
    str, dict[int, list[renpy.ast.Python | renpy.ast.Define | renpy.ast.Default | renpy.ast.EarlyPython]]
]


def get_statements_from_rpy(fname: str) -> list[renpy.ast.Node] | None:
    renpy.parser.parse_errors.clear()

    lines = renpy.parser.list_logical_lines(fname, None, 1)
    nested = renpy.parser.group_logical_lines(lines)
    l = renpy.parser.Lexer(nested)
    statements = renpy.parser.parse_block(l)

    return statements


def extract_python_nodes(statements: list[renpy.ast.Node]) -> InitNodes:

    init_nodes: InitNodes = {}

    def process_node(node: renpy.ast.Node, priority: int | None = None) -> None:
        if isinstance(node, renpy.ast.EarlyPython):
            if node.hide:
                return
            init_nodes.setdefault(node.store, {}).setdefault(EARLY_PRIORITY, []).append(node)

        elif isinstance(node, renpy.ast.Python):
            if node.hide:
                return

            if priority is None:
                raise renpy.script.ScriptError("Python block found outside of Init block.")
            init_nodes.setdefault(node.store, {}).setdefault(priority, []).append(node)

        elif isinstance(node, (renpy.ast.Define, renpy.ast.Default)):
            if priority is None:
                raise renpy.script.ScriptError("Define/Default block found outside of Init block.")
            init_nodes.setdefault(node.store, {}).setdefault(priority, []).append(node)

    for stmt in statements:
        if isinstance(stmt, renpy.ast.Init):
            for node in stmt.block:
                process_node(node, stmt.priority)
        else:
            process_node(stmt)

    for k, v in init_nodes.items():
        init_nodes[k] = dict(sorted(v.items(), key=lambda x: x[0]))
    init_nodes = dict(sorted(init_nodes.items()))
    return init_nodes


def generate_py_content(init_nodes: InitNodes) -> dict[str, str]:
    rv: dict[str, str] = {}

    def dedent(txt: str) -> str:
        dedented_text = ""
        space: str | None = None

        for line in txt.splitlines():
            if space is None:
                stripped = line.lstrip()
                if stripped:
                    space = line[: len(line) - len(stripped)]
                else:
                    dedented_text += "\n"
                    continue

            if space and line.startswith(space):
                dedented_text += line[len(space) :] + "\n"
            else:
                dedented_text += line + "\n"

        return dedented_text

    for store, nodes_dict in init_nodes.items():
        content = ""
        for priority, nodes in nodes_dict.items():
            if not nodes:
                continue

            content += f"\n# Init block priority: {priority}\n"

            for node in nodes:
                if isinstance(node, (renpy.ast.Python, renpy.ast.EarlyPython)):
                    content += dedent(node.code.source) + "\n"

                elif isinstance(node, (renpy.ast.Define, renpy.ast.Default)):
                    content += f"{node.varname} = {node.code.source}\n"

        if content:
            store_class_name = store or "store"
            rv[store_class_name] = content

    return rv


def main():
    if not renpy.game.script:
        raise RuntimeError("Failed to initialize Ren'Py script.")

    ## Target .rpy and .rpym files
    num_files = 0
    fnames: list[str] = []
    # TODO: Temporarily disabled to check the full merge-generate cycle
    # fnames.extend(glob.glob(str(config.renpy_path) + "/renpy/**/*.rpy", recursive=True, include_hidden=True))
    # fnames.extend(glob.glob(str(config.renpy_path) + "/renpy/**/*.rpym", recursive=True, include_hidden=True))
    # fnames.extend(glob.glob(str(config.renpy_path) + "/renpy/common/**/*_ren.py", recursive=True, include_hidden=True))

    for fname in fnames:
        statements = get_statements_from_rpy(fname)

        if not statements:
            continue

        try:
            init_nodes = extract_python_nodes(statements)
            content = generate_py_content(init_nodes)

            if not content:
                continue

            for store, content in content.items():
                # Determine output path (renpy/store/substore/module.py)
                output_path = config.rpy_extraction_temp_path / "renpy"
                for part in store.split("."):
                    output_path = output_path / part
                output_path = output_path / Path(fname).name
                output_path = output_path.with_suffix(".py")

                ## Replace leading numbers with __numbered_ in filename (eg. 000atl.rpy -> __numbered_atl.py)
                output_path = output_path.with_name(
                    "__numbered_" + "".join(c if not c.isdigit() else "" for c in output_path.name)
                )
                output_path.parent.mkdir(parents=True, exist_ok=True)

                num_files += 1
                with open(output_path, "a", encoding="utf-8") as f:
                    f.write("\n" + content)

        except renpy.script.ScriptError as e:
            print(f"Error processing statement in {fname}: {e}")
            continue

    print(f"Extracted Python code from {num_files} Ren'Py files.")


if __name__ == "__main__":
    main()
