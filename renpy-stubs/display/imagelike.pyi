import renpy
from _typeshed import Incomplete
from renpy.compat import (
    PY2 as PY2,
    basestring as basestring,
    bchr as bchr,
    bord as bord,
    chr as chr,
    open as open,
    pystr as pystr,
    range as range,
    round as round,
    str as str,
    tobytes as tobytes,
    unicode as unicode,
)
from renpy.display.matrix import Matrix2D as Matrix2D
from renpy.display.render import Render as Render, render as render

class Solid(renpy.display.displayable.Displayable):
    color: Incomplete
    def __init__(self, color, **properties) -> None: ...
    def __hash__(self): ...
    def __eq__(self, o): ...
    def visit(self): ...
    def render(self, width, height, st, at): ...

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
        self, left, top, right, bottom, pad_left: int = 0, pad_top: int = 0, pad_right: int = 0, pad_bottom: int = 0
    ) -> None: ...
    @property
    def padding(self): ...

class Frame(renpy.display.displayable.Displayable):
    __version__: int
    properties: Incomplete
    tile_ratio: float
    left: Incomplete
    right: Incomplete
    top: Incomplete
    bottom: Incomplete
    def after_upgrade(self, version) -> None: ...
    image: Incomplete
    tile: Incomplete
    def __init__(
        self,
        image,
        left=None,
        top=None,
        right=None,
        bottom=None,
        xborder: int = 0,
        yborder: int = 0,
        bilinear: bool = True,
        tile: bool = False,
        tile_ratio: float = 0.5,
        **properties,
    ) -> None: ...
    def __eq__(self, o): ...
    def render(self, width, height, st, at): ...
    def draw_pattern(self, draw, left, top, right, bottom) -> None: ...
    def sw_render(self, crend, dw, dh, left, top, right, bottom): ...
    def visit(self): ...

class FileCurrentScreenshot(renpy.display.displayable.Displayable):
    empty: Incomplete
    def __init__(self, empty=None, **properties) -> None: ...
    def render(self, width, height, st, at): ...
