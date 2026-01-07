from _frozen_importlib import BuiltinImporter as BuiltinImporter
from _typeshed import Incomplete
from types import IO

class FTFace:
    def __init__(self, f: IO, index: int, fn: str) -> None: ...

class FTFont:
    def __init__(
        self,
        face: FTFace,
        size: float,
        bold: float,
        italic: bool,
        outline: int,
        antialias: bool,
        vertical: bool,
        hinting: str | None,
    ) -> None: ...
    def bounds(self, glyphs: Incomplete, bounds: Incomplete) -> Incomplete: ...
    def draw(
        self,
        pysurf: Incomplete,
        xo: float,
        yo: int,
        color: Incomplete,
        glyphs: list,
        underline: int,
        strikethrough: bool,
        black_color: Incomplete,
    ) -> Incomplete: ...
    def glyphs(self, s: str, level: int) -> Incomplete: ...

class FreetypeError(Exception):
    def __init__(self, code: Incomplete) -> None: ...

def init() -> None: ...
