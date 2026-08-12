from _frozen_importlib import BuiltinImporter as BuiltinImporter
from typing import IO, Literal
from renpy.pygame.surface import Surface
from renpy.text.textsupport import Glyph

type FeatureType = tuple[str, int]

class Axis:
    def __init__(self, index: int, minimum: float, default: float, maximum: float) -> None: ...

class Features:
    def __init__(self, features: list[FeatureType]) -> None: ...
    @staticmethod
    def get(features: list[FeatureType]) -> Features: ...

class FreetypeError(Exception):
    def __init__(self, code: int) -> None: ...

class HBFace:
    def __init__(self, f: IO, index: int, fn: str) -> None: ...

class HBFont:
    def __init__(
        self,
        face: HBFace,
        size: float,
        bold: float,
        italic: bool,
        outline: int,
        antialias: bool,
        vertical: bool,
        hinting: str | None,
        instance: Literal["bold", "bold italic", "regular", "italic"] | None,
        axis: dict[str, Axis] | None,
        features: list[FeatureType] | None,
    ) -> None: ...
    def bounds(self, glyphs: list[Glyph], bounds: tuple[int, int, int, int]) -> tuple[int, int, int, int]: ...
    def draw(
        self,
        pysurf: Surface,
        xo: float,
        yo: int,
        color: tuple[int, int, int, int],
        glyphs: list[Glyph],
        underline: int,
        strikethrough: bool,
        black_color: tuple[int, int, int, int] | None,
    ) -> None: ...
    def glyphs(self, s: str, level: int) -> list[Glyph]: ...

class Variations:
    def __init__(self) -> None: ...

def init() -> None: ...
