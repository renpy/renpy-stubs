import renpy
from _typeshed import Incomplete
from renpy.display.displayable import Displayable as Displayable
from renpy.display.matrix import Matrix2D as Matrix2D
from renpy.display.render import Render as Render, render as render
from renpy.types import DisplayableLike as DisplayableLike, Unused as Unused
from typing import Callable, Self

class Solid(Displayable):
    color: Incomplete
    def __init__(self, color: renpy.color.ColorLike | None, **properties) -> None: ...
    def __hash__(self) -> int: ...
    def __eq__(self, o: object) -> bool: ...
    def visit(self) -> list[Displayable]: ...
    def render(self, width: float, height: float, st: float, at: float) -> Render: ...

class Borders:
    left: Incomplete
    top: Incomplete
    right: Incomplete
    bottom: Incomplete
    pad_left: Incomplete
    pad_top: Incomplete
    pad_right: Incomplete
    pad_bottom: Incomplete
    def __init__(
        self,
        left: int,
        top: int,
        right: int,
        bottom: int,
        pad_left: int = 0,
        pad_top: int = 0,
        pad_right: int = 0,
        pad_bottom: int = 0,
    ) -> None: ...
    @property
    def padding(self) -> tuple[int, int, int, int]: ...

class Frame(Displayable):
    __version__: int
    properties: Unused
    tile_ratio: float
    left: Incomplete
    right: Incomplete
    top: Incomplete
    bottom: Incomplete
    def after_upgrade(self, version: int) -> None: ...
    image: Incomplete
    _duplicatable: Incomplete
    tile: Incomplete
    def __init__(
        self,
        image: DisplayableLike,
        left: int | Borders | None = None,
        top: int | None = None,
        right: int | None = None,
        bottom: int | None = None,
        xborder: int = 0,
        yborder: int = 0,
        bilinear: bool = True,
        tile: bool = False,
        tile_ratio: float = 0.5,
        **properties,
    ) -> None: ...
    def __repr__(self) -> str: ...
    def __eq__(self, o: object) -> bool: ...
    def render(self, width: float, height: float, st: float, at: float) -> Render: ...
    def draw_pattern(
        self, draw: Callable[[float, float, float, float], None], left: float, top: float, right: float, bottom: float
    ) -> None: ...
    def sw_render(
        self, crend: Render, dw: float, dh: float, left: float, top: float, right: float, bottom: float
    ) -> Render: ...
    def _duplicate(self, args: Incomplete) -> Incomplete: ...
    def _unique(self) -> None: ...
    def _in_current_store(self) -> Self: ...
    def visit(self) -> list[Displayable]: ...

class FileCurrentScreenshot(Displayable):
    empty: Incomplete
    def __init__(self, empty: Displayable | None = None, **properties) -> None: ...
    def render(self, width: float, height: float, st: float, at: float) -> Render: ...
