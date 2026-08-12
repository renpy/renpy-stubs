import sys
import argparse
from pathlib import Path

def add_project_to_path():
    """
    Add the project base directory to sys.path for module imports.
    """

    project_base = Path(__file__).resolve().parent
    sys.path.append(str(project_base))


def main():
    add_project_to_path()

    parser = argparse.ArgumentParser(prog=str(Path(sys.argv[0]).name))
    parser.add_argument("--path", help="Path to the Ren'Py repository")

    subparsers = parser.add_subparsers(dest="command", help="script to run")

    subparsers.add_parser("extract", help="Extract type data from renpy files and update stubs")
    subparsers.add_parser("inject", help="Inject type data from stubs into renpy source files")

    parsed, remaining = parser.parse_known_args()

    if parsed.path:
        from config import config

        config.renpy_path = parsed.path

    if not parsed.command:
        parser.print_help()
        return

    if parsed.command == "extract":
        from scripts import extract

        extract.main()
    elif parsed.command == "inject":
        from scripts import inject

        sys.argv = [sys.argv[0]] + remaining
        inject.main()
    else:
        print(f"Error: Unknown command {parsed.command}")
        sys.exit(1)


if __name__ == "__main__":
    main()
