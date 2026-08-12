import os
import sys
import argparse


def add_project_to_path():
    """
    Add the project base directory to sys.path for module imports.
    """

    project_base = os.path.dirname(os.path.abspath(__file__))
    project_base = os.path.abspath(project_base)

    sys.path.append(project_base)


def main():
    add_project_to_path()

    parser = argparse.ArgumentParser(prog=os.path.basename(sys.argv[0]))
    subparsers = parser.add_subparsers(dest="command", help="script to run")

    subparsers.add_parser("generate", help="Run scripts.generate_pyi")
    subparsers.add_parser("merge", help="Run scripts.merge_pyi")

    parsed, remaining = parser.parse_known_args()

    if not parsed.command:
        parser.print_help()
        return

    from scripts import generate_pyi, merge_pyi

    if parsed.command == "generate":
        generate_pyi.main()
    elif parsed.command == "merge":
        merge_pyi.main()
    else:
        print(f"Error: Unknown command {parsed.command}")
        sys.exit(1)


if __name__ == "__main__":
    main()
