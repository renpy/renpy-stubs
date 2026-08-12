import sys
from pathlib import Path


class Config:
    _renpy_path: Path
    "Renpy directory containing .py files."

    _pyi_path: Path
    "Directory where generated .pyi stub files will be placed."

    rpy_extraction_temp_path: Path
    "Used for storing temporary .py files extracted from .rpy files."

    temp_gen_path: Path
    "Used for storing temporary files during generation."

    renpy_python: str
    "Path to Ren'Py's bundled Python executable. Auto-detected if empty."

    exclude_files: list[str]
    "List of files to exclude from stub generation."

    def __init__(self, renpy_dir: str = "../../", temp_rpy_dir: str = "temp/rpy/", temp_gen_dir: str = "temp/gen/"):
        base_dir = Path.cwd()

        self.renpy_path = renpy_dir
        self.pyi_path = "./src"
        self.rpy_extraction_temp_path = base_dir / temp_rpy_dir
        self.temp_gen_path = base_dir / temp_gen_dir

        self.exclude_files = [
            "renpy/common/",
            "renpy/compat/pickle.py",
            "renpy/gl2/gl2shadercache.py",
            "renpy/object.py",
            "renpy/pygame/compat.py",
            "renpy/revertable.py",
            "renpy/test/testsettings.py",
            "renpy/text/emoji_trie.py",  # Invalid characters
            "renpy/types.py",
        ]

    @property
    def pyi_path(self) -> Path:
        return self._pyi_path

    @pyi_path.setter
    def pyi_path(self, value):
        v = Path(value).resolve()
        if not v.is_dir():
            print(f"Pyi directory does not exist: {v}", file=sys.stderr)
            sys.exit(2)
        self._pyi_path = v

    @property
    def renpy_path(self) -> Path:
        return self._renpy_path

    @renpy_path.setter
    def renpy_path(self, value):
        v = Path(value).resolve()
        if not v.is_dir():
            print(f"Renpy directory does not exist: {value} -> {v}", file=sys.stderr)
            sys.exit(2)
        self._renpy_path = v

        # Auto-detect renpy's Python executable based on the platform.
        if sys.platform.startswith("win"):
            python_path = v / "lib" / "py3-windows-x86_64" / "python.exe"
        elif sys.platform == "darwin":
            python_path = v / "lib" / "py3-mac-universal" / "python"
        else:  # Linux and other POSIX
            python_path = v / "lib" / "py3-linux-x86_64" / "python"

        if not python_path.is_file():
            raise FileNotFoundError(f"Could not find python executable in libs/")

        self.renpy_python = str(python_path.resolve())


config = Config()
