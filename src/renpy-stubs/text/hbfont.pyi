from _frozen_importlib import BuiltinImporter as BuiltinImporter
from _typeshed import Incomplete
from typing import IO

class Axis:
    def __init__(self, index: Incomplete, minimum: Incomplete, default: Incomplete, maximum: Incomplete) -> None: ...

class Features:
    def __init__(self, features: Incomplete) -> None: ...
    def __reduce__(self) -> str | tuple[Any, ...]: ...
    @staticmethod
    def get(features: Incomplete) -> None: ...

class FreetypeError(Exception):
    def __init__(self, code: Incomplete) -> None: ...

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
        instance: Incomplete,
        axis: Incomplete,
        features: Incomplete,
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

class Variations:
    def __init__(self) -> None: ...

def init() -> None: ...
