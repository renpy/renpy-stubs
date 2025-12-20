import renpy
from _typeshed import Incomplete as Incomplete
from renpy.color import ColorLike as ColorLike
from renpy.display.displayable import Displayable as Displayable, Placement as Placement
from renpy.display.im import ImageLike as ImageLike
from renpy.display.render import Render as Render, render as render
from renpy.types import DisplayableLike as DisplayableLike, Unused as Unused
from typing import Any, Protocol, overload, type_check_only

type Warper = renpy.atl.Warper

@type_check_only
class TransitionFunction(Protocol):
    def __call__(self, old_widget: Displayable | None, new_widget: Displayable | None) -> Transition: ...

class Transition(renpy.display.displayable.Displayable):
    new_widget: Displayable | None
    old_widget: Displayable | None
    delay: float
    events: bool
    def __init__(self, delay: float, **properties) -> None: ...
    def event(self, ev: renpy.pygame.event.EventType, x: float, y: float, st: float) -> Any | None: ...
    def visit(self) -> list[Displayable | None]: ...
    def get_placement(self) -> Placement: ...

def null_render(d: Transition, width: float, height: float, st: float, at: float) -> Render: ...

class NoTransition(Transition):
    old_widget: Displayable | None
    new_widget: Displayable | None
    events: bool
    def __init__(
        self, delay: float, old_widget: Displayable | None = None, new_widget: Displayable | None = None, **properties
    ) -> None: ...
    def render(self, width: float, height: float, st: float, at: float) -> Render: ...

class MultipleTransition(Transition):
    transitions: list[Transition]
    screens: list[Displayable]
    new_widget: Displayable | None
    events: bool
    def __init__(
        self,
        args: Incomplete,
        old_widget: Displayable | None = None,
        new_widget: Displayable | None = None,
        **properties,
    ) -> None: ...
    def visit(self) -> list[Displayable]: ...
    def event(self, ev: renpy.pygame.event.EventType, x: float, y: float, st: float) -> Any | None: ...
    def render(self, width: float, height: float, st: float, at: float) -> Render: ...

def Fade(
    out_time: float,
    hold_time: float,
    in_time: float,
    old_widget: Displayable | None = None,
    new_widget: Displayable | None = None,
    color: ColorLike | None = None,
    widget: Displayable | None = None,
    alpha: bool = False,
) -> MultipleTransition: ...

class Pixellate(Transition):
    time: float
    steps: int
    old_widget: Displayable | None
    new_widget: Displayable | None
    events: bool
    quantum: float
    def __init__(
        self,
        time: float,
        steps: int,
        old_widget: Displayable | None = None,
        new_widget: Displayable | None = None,
        **properties,
    ) -> None: ...
    def render(self, width: float, height: float, st: float, at: float) -> Render: ...

class Dissolve(Transition):
    __version__: int
    alpha: bool
    def after_upgrade(self, version: int) -> None: ...
    time_warp: Warper | None
    time: float
    old_widget: Displayable | None
    new_widget: Displayable | None
    events: bool
    def __init__(
        self,
        time: float,
        old_widget: Displayable | None = None,
        new_widget: Displayable | None = None,
        alpha: bool = False,
        time_warp: Warper | None = None,
        **properties,
    ) -> None: ...
    def render(self, width: float, height: float, st: float, at: float) -> Render: ...

class ImageDissolve(Transition):
    __version__: int
    alpha: bool
    def after_upgrade(self, version: int) -> None: ...
    time_warp: Warper | None
    old_widget: Displayable | None
    new_widget: Displayable | None
    events: bool
    image: Displayable
    ramplen: int
    def __init__(
        self,
        image: ImageLike,
        time: float,
        ramplen: int = 8,
        ramptype: str = "linear",
        ramp: list | None = None,
        reverse: bool = False,
        alpha: bool = False,
        old_widget: Displayable | None = None,
        new_widget: Displayable | None = None,
        time_warp: Warper | None = None,
        **properties,
    ) -> None: ...
    def visit(self) -> list[Displayable | None]: ...
    def render(self, width: float, height: float, st: float, at: float) -> Render: ...

class AlphaDissolve(Transition):
    mipmap: Unused
    control: renpy.display.layout.MultiBox
    old_widget: Displayable | None
    new_widget: Displayable | None
    events: bool
    alpha: bool
    reverse: bool
    def __init__(
        self,
        control: DisplayableLike,
        delay: float = 0.0,
        old_widget: Displayable | None = None,
        new_widget: Displayable | None = None,
        alpha: bool = False,
        reverse: bool = False,
        **properties,
    ) -> None: ...
    def visit(self) -> list[Displayable | None]: ...
    def render(self, width: float, height: float, st: float, at: float) -> Render: ...

@overload
def interpolate_tuple[T](t0: tuple[T], t1: tuple[T], time: float, scales: tuple[float, ...]) -> tuple[T]: ...
@overload
def interpolate_tuple[T](t0: tuple[T, T], t1: tuple[T, T], time: float, scales: tuple[float, ...]) -> tuple[T, T]: ...
@overload
def interpolate_tuple[T](
    t0: tuple[T, T, T], t1: tuple[T, T, T], time: float, scales: tuple[float, ...]
) -> tuple[T, T, T]: ...
@overload
def interpolate_tuple[T](
    t0: tuple[T, T, T, T], t1: tuple[T, T, T, T], time: float, scales: tuple[float, ...]
) -> tuple[T, T, T, T]: ...

class CropMove(Transition):
    time: float
    delay: float
    startpos: tuple[float, float]
    endpos: tuple[float, float]
    startcrop: tuple[float, float, float, float]
    endcrop: tuple[float, float, float, float]
    topnew: bool
    old_widget: Displayable | None
    new_widget: Displayable | None
    events: bool
    bottom: Displayable | None
    top: Displayable | None
    def __init__(
        self,
        time: float,
        mode: str = "slideright",
        startcrop: tuple[float, float, float, float] = (0.0, 0.0, 0.0, 1.0),
        startpos: tuple[float, float] = (0.0, 0.0),
        endcrop: tuple[float, float, float, float] = (0.0, 0.0, 1.0, 1.0),
        endpos: tuple[float, float] = (0.0, 0.0),
        topnew: bool = True,
        old_widget: Displayable | None = None,
        new_widget: Displayable | None = None,
        **properties,
    ) -> None: ...
    def render(self, width: float, height: float, st: float, at: float) -> Render: ...

class PushMove(Transition):
    time: float
    new_startpos: tuple[float, float]
    new_startcrop: tuple[float, float, float, float]
    new_endpos: tuple[float, float]
    new_endcrop: tuple[float, float, float, float]
    old_endpos: tuple[float, float]
    old_endcrop: tuple[float, float, float, float]
    old_startpos: tuple[float, float]
    old_startcrop: tuple[float, float, float, float]
    delay: float
    old_widget: Displayable | None
    new_widget: Displayable | None
    events: bool
    def __init__(
        self,
        time: float,
        mode: str = "pushright",
        old_widget: Displayable | None = None,
        new_widget: Displayable | None = None,
        **properties,
    ) -> None: ...
    def render(self, width: float, height: float, st: float, at: float) -> Render: ...

def ComposeTransition(
    trans: TransitionFunction,
    before: TransitionFunction | None = None,
    after: TransitionFunction | None = None,
    new_widget: Displayable | None = None,
    old_widget: Displayable | None = None,
) -> Displayable: ...
def SubTransition(
    rect,
    trans: TransitionFunction,
    old_widget: Displayable | None = None,
    new_widget: Displayable | None = None,
    **properties,
) -> NoTransition: ...
