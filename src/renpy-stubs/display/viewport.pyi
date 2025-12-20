import renpy
import renpy.pygame as pygame
from renpy.display.layout import Container as Container
from renpy.types import DisplayableLike as DisplayableLike
from typing import Callable, Literal

def edgescroll_proportional(n: float) -> float: ...

class Viewport(renpy.display.layout.Container):
    __version__: int
    arrowkeys: bool
    pagekeys: bool
    _draggable: bool
    drag_position_time: float | None
    xadjustment: renpy.ui.Adjustment | None
    yadjustment: renpy.ui.Adjustment | None
    set_adjustments: bool
    mousewheel: bool
    draggable: bool
    width: int
    height: int
    drag_position: tuple[float, float] | None
    edge_size: bool
    edge_speed: Literal[False] | float
    edge_function: Callable[[float], float] | None
    edge_xspeed: int
    edge_yspeed: int
    edge_last_st: float | None
    focusable: bool | None
    def after_upgrade(self, version: int) -> None: ...
    xoffset: int | float | None
    yoffset: int | float | None
    drag_speed: tuple[float, float] | None
    def __init__(
        self,
        child: DisplayableLike | None = None,
        child_size: tuple[int | None, int | None] = (None, None),
        offsets: tuple[int | None, int | None] = (None, None),
        xadjustment: renpy.ui.Adjustment | None = None,
        yadjustment: renpy.ui.Adjustment | None = None,
        set_adjustments: bool = True,
        mousewheel: bool = False,
        draggable: bool = False,
        edgescroll: tuple[tuple[float, float], float]
        | tuple[tuple[float, float], float, Callable[[float], float]]
        | None = None,
        style: str = "viewport",
        xinitial: int | float | None = None,
        yinitial: int | float | None = None,
        replaces: Viewport | None = None,
        arrowkeys: bool = False,
        pagekeys: bool = False,
        **properties,
    ) -> None: ...
    def per_interact(self) -> None: ...
    def set_style_prefix(self, prefix: str, root: bool) -> None: ...
    def update_offsets(self, cw: float, ch: float, st: float) -> tuple[int, int, float, float]: ...
    offsets: list[tuple[int, int]]
    def render(self, width: float, height: float, st: float, at: float) -> renpy.display.render.Render: ...
    def check_edge_redraw(self, st: float, reset_st: bool = True) -> None: ...
    def event(self, ev: pygame.event.EventType, x: float, y: float, st: float) -> None: ...
    def set_xoffset(self, offset: int | float | None) -> None: ...
    def set_yoffset(self, offset: int | float | None) -> None: ...

class VPGrid(Viewport):
    __version__: int
    allow_underfull: bool | None
    grid_cols: int | None
    grid_rows: int | None
    grid_transpose: bool | None
    def __init__(
        self,
        cols: int | None = None,
        rows: int | None = None,
        transpose: bool | None = None,
        style: str = "vpgrid",
        allow_underfull: bool | None = None,
        **properties,
    ) -> None: ...
    width: int
    height: int
    offsets: list[tuple[int, int]]
    def render(self, width: float, height: float, st: float, at: float) -> renpy.display.render.Render: ...
    def add(self, d: DisplayableLike) -> None: ...
    def per_interact(self) -> None: ...
