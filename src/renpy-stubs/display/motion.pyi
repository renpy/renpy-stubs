import renpy
from _typeshed import Incomplete as Incomplete
from renpy.display.displayable import Displayable as Displayable, Placement as Placement
from renpy.display.layout import Container as Container
from renpy.display.position import absolute as absolute
from renpy.display.render import Render as Render, render as render
from renpy.display.transform import (
    ATLTransform as ATLTransform,
    Proxy as Proxy,
    Transform as Transform,
    TransformState as TransformState,
    null as null,
)
from renpy.types import DisplayableLike as DisplayableLike, Unused as Unused
from renpy.pygame.event import EventType
from typing import Any, Callable, Literal, Sequence

type SizeRect = tuple[float | None, float | None, float | None, float | None]

class Motion(Container):
    function: Callable[[float, SizeRect], Incomplete]
    period: float
    repeat: bool
    bounce: bool
    delay: float | None
    anim_timebase: bool
    time_warp: Callable[[float], float] | None
    add_sizes: bool
    position: SizeRect | None
    def __init__(
        self,
        function: Callable[[float, SizeRect], Incomplete],
        period: float,
        child: Displayable | None = None,
        new_widget: Displayable | None = None,
        old_widget: Displayable | None = None,
        repeat: bool = False,
        bounce: bool = False,
        delay: float | None = None,
        anim_timebase: bool = False,
        tag_start: Unused = None,
        time_warp: Callable[[float], float] | None = None,
        add_sizes: bool = False,
        style: str = "motion",
        **properties,
    ) -> None: ...
    def update_position(self, t: float, sizes: SizeRect) -> None: ...
    def get_placement(self) -> Placement: ...
    offsets: list[tuple[Literal[0], Literal[0]]] | Unused
    def render(self, width: float, height: float, st: float, at: float) -> Render: ...

class Interpolate:
    anchors: dict[str, float]
    start: list[float]
    end: list[float]
    def __init__(self, start: Sequence[str | float], end: Sequence[str | float]) -> None: ...
    def __call__(self, t: float, sizes: SizeRect = (None, None, None, None)) -> list[float]: ...

def Pan(
    startpos: tuple[float, float],
    endpos: tuple[float, float],
    time: float,
    child: Displayable | None = None,
    repeat: bool = False,
    bounce: bool = False,
    anim_timebase: bool = False,
    style: str = "motion",
    time_warp: Callable[[float], float] | None = None,
    **properties,
) -> Motion: ...
def Move(
    startpos: tuple[float, float],
    endpos: tuple[float, float],
    time: float,
    child: Displayable | None = None,
    repeat: bool = False,
    bounce: bool = False,
    anim_timebase: bool = False,
    style: str = "motion",
    time_warp: Callable[[float], float] | None = None,
    **properties,
) -> Motion: ...

class Revolver:
    start: float
    end: float
    around: tuple[float, float]
    cor: tuple[float, float]
    pos: Placement | None
    child: Displayable
    def __init__(
        self,
        start: float,
        end: float,
        child: Displayable,
        around: tuple[float, float] = (0.5, 0.5),
        cor: tuple[float, float] = (0.5, 0.5),
        pos: Placement | None = None,
    ) -> None: ...
    def __call__(self, t: float, rect: SizeRect) -> tuple[absolute, absolute, Literal[0], Literal[0]]: ...

def Revolve(
    start: float,
    end: float,
    time: float,
    child: Displayable,
    around: tuple[float, float] = (0.5, 0.5),
    cor: tuple[float, float] = (0.5, 0.5),
    pos: Placement | None = None,
    **properties,
) -> Motion: ...
def zoom_render(
    crend: Render, x: float, y: float, w: float, h: float, zw: float, zh: float, bilinear: bool
) -> Render: ...

class ZoomCommon(renpy.display.displayable.Displayable):
    time: float
    child: Displayable
    repeat: bool
    after_child: Displayable | None
    time_warp: Callable[[float], float] | None
    bilinear: bool
    opaque: bool
    anim_timebase: bool
    def __init__(
        self,
        time: float,
        child: DisplayableLike,
        end_identity: bool = False,
        after_child: DisplayableLike | None = None,
        time_warp: Callable[[float], float] | None = None,
        bilinear: bool = True,
        opaque: bool = True,
        anim_timebase: bool = False,
        repeat: bool = False,
        style: str = "motion",
        **properties,
    ) -> None: ...
    def visit(self) -> list[Displayable | None]: ...
    def zoom_rectangle(
        self, done: float, width: float, height: float
    ) -> tuple[float, float, float, float, float, float]: ...
    done: float
    def render(self, width: float, height: float, st: float, at: float) -> Render: ...
    def event(self, ev: EventType, x: float, y: float, st: float) -> Any | None: ...

class Zoom(ZoomCommon):
    size: tuple[float, float]
    start: tuple[float, float]
    end: tuple[float, float]
    def __init__(
        self,
        size: tuple[float, float],
        start: tuple[float, float],
        end: tuple[float, float],
        time: float,
        child: DisplayableLike,
        **properties,
    ) -> None: ...
    def zoom_rectangle(
        self, done: float, width: float, height: float
    ) -> tuple[float, float, float, float, float, float]: ...

class FactorZoom(ZoomCommon):
    start: float
    end: float
    def __init__(self, start: float, end: float, time: float, child: DisplayableLike, **properties) -> None: ...
    def zoom_rectangle(
        self, done: float, width: float, height: float
    ) -> tuple[float, float, float, float, float, float]: ...

class SizeZoom(ZoomCommon):
    start: tuple[float, float]
    end: tuple[float, float]
    def __init__(
        self, start: tuple[float, float], end: tuple[float, float], time: float, child: DisplayableLike, **properties
    ) -> None: ...
    def zoom_rectangle(
        self, done: float, width: float, height: float
    ) -> tuple[float, float, float, float, float, float]: ...

class RotoZoom(renpy.display.displayable.Displayable):
    transform: Transform | None
    rot_start: float
    rot_end: float
    rot_delay: float
    zoom_start: float
    zoom_end: float
    zoom_delay: float
    child: Displayable
    rot_repeat: bool
    zoom_repeat: bool
    rot_bounce: bool
    zoom_bounce: bool
    rot_anim_timebase: bool
    zoom_anim_timebase: bool
    rot_time_warp: Callable[[float], float] | None
    zoom_time_warp: Callable[[float], float] | None
    opaque: bool
    def __init__(
        self,
        rot_start: float,
        rot_end: float,
        rot_delay: float,
        zoom_start: float,
        zoom_end: float,
        zoom_delay: float,
        child: DisplayableLike,
        rot_repeat: bool = False,
        zoom_repeat: bool = False,
        rot_bounce: bool = False,
        zoom_bounce: bool = False,
        rot_anim_timebase: bool = False,
        zoom_anim_timebase: bool = False,
        rot_time_warp: Callable[[float], float] | None = None,
        zoom_time_warp: Callable[[float], float] | None = None,
        opaque: bool = False,
        style: str = "motion",
        **properties,
    ) -> None: ...
    def visit(self) -> list[Displayable]: ...
    def render(self, width: float, height: float, st: float, at: float) -> Render: ...
