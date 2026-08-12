import os
from dataclasses import dataclass, InitVar, field
import sys
import json
from pathlib import Path

USER_CONFIG_FILE = "config.json"


@dataclass
class Config:
    renpy_dir: InitVar[str] = "../renpy/"
    renpy_path: Path = field(init=False)
    "Renpy directory containing .py files."

    pyi_dir: InitVar[str] = "src/"
    pyi_path: Path = field(init=False)
    "Directory where generated .pyi stub files will be placed."

    rpy_extraction_temp_dir: InitVar[str] = "temp/rpy/"
    rpy_extraction_temp_path: Path = field(init=False)
    "Used for storing temporary .py files extracted from .rpy files."

    temp_gen_dir: InitVar[str] = "temp/gen/"
    temp_gen_path: Path = field(init=False)
    "Used for storing temporary files during generation."

    exclude_files: list[str] = field(default_factory=lambda: ["renpy/pygame/compat.py", "renpy/common/"])
    "List of files to exclude from stub generation."

    def __post_init__(self, renpy_dir: str, pyi_dir: str, temp_rpy_dir: str, temp_gen_dir: str):
        base_dir = Path(__file__).parent.parent.resolve()

        self.renpy_path = base_dir / renpy_dir
        self.pyi_path = base_dir / pyi_dir
        self.rpy_extraction_temp_path = base_dir / temp_rpy_dir
        self.temp_gen_path = base_dir / temp_gen_dir

        self.validate()

    def validate(self):
        if not self.pyi_path.is_dir():
            print(f"Pyi directory does not exist: {self.pyi_path}", file=sys.stderr)
            sys.exit(2)
        if not self.renpy_path.is_dir():
            print(f"Renpy directory does not exist: {self.renpy_path}", file=sys.stderr)
            sys.exit(2)


def load_user_config() -> Config:
    """
    Loads the user configuration, creating it from the default if necessary.
    """
    base_dir = Path(__file__).parent.parent.resolve()

    # Overwrite with user config if it exists
    if os.path.exists(base_dir / USER_CONFIG_FILE):
        with open(base_dir / USER_CONFIG_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        rv = Config(**data)
    else:
        rv = Config()

    return rv


config = load_user_config()
