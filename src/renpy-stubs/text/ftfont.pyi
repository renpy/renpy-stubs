from _frozen_importlib import BuiltinImporter as BuiltinImporter
from typing import IO
from renpy.text.textsupport import Glyph
from renpy.pygame.surface import Surface

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
    def bounds(self, glyphs: list[Glyph], bounds: tuple[int, int, int, int]) -> tuple[int, int, int, int]: ...
    def draw(
        self,
        pysurf: Surface,
        xo: float,
        yo: int,
        color: tuple[int, int, int, int],
        glyphs: list,
        underline: int,
        strikethrough: bool,
        black_color: tuple[int, int, int, int] | None,
    ) -> None: ...
    def glyphs(self, s: str, level: int) -> list[Glyph]: ...

class FreetypeError(Exception):
    def __init__(self, code: int) -> None: ...

def init() -> None: ...
