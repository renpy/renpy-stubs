import renpy
from _typeshed import Incomplete as Incomplete
from renpy.display.displayable import Displayable as Displayable, Placement as Placement
from renpy.display.layout import MultiBox as MultiBox
from renpy.types import DisplayableLike as DisplayableLike, Unused as Unused
from typing import Callable

type Rect = tuple[float, float, float, float]
type Factory = Callable[[Rect, Rect, float, MultiBox], MultiBox]
type EnterFactory = Callable[[Rect, float, MultiBox], MultiBox]
type LeaveFactory = Callable[[Rect, float, MultiBox], None]
type WarpFunction = Callable[[float], float]

def position(d: Displayable) -> tuple[float, float, float, float]: ...
def offsets(d: Displayable) -> dict[str, float | None]: ...
def MoveFactory(pos1: Rect, pos2: Rect, delay: float, d: MultiBox, **kwargs) -> MultiBox: ...
def default_enter_factory(pos: Rect, delay: float, d: MultiBox, **kwargs) -> MultiBox: ...
def default_leave_factory(pos: Rect, delay: float, d: MultiBox, **kwargs) -> None: ...
def MoveIn(
    pos: tuple[float, float], pos1: tuple[float, float], delay: float, d: Incomplete, **kwargs
) -> Incomplete: ...
def MoveOut(
    pos: tuple[float, float], pos1: tuple[float, float], delay: float, d: Incomplete, **kwargs
) -> Incomplete: ...
def ZoomInOut(start: float, end: float, pos: Rect, delay: float, d: Incomplete, **kwargs) -> Incomplete: ...
def RevolveInOut(start: float, end: float, pos: Rect, delay: float, d: Incomplete, **kwargs) -> Incomplete: ...
def OldMoveTransition(
    delay: float,
    old_widget: Displayable | None = None,
    new_widget: Displayable | None = None,
    factory: Factory | None = None,
    enter_factory: EnterFactory | None = None,
    leave_factory: LeaveFactory | None = None,
    old: bool = False,
    layers: list[str] = ["master"],
) -> MultiBox: ...

class MoveInterpolate(renpy.display.displayable.Displayable):
    old: MultiBox
    new: MultiBox
    use_old: bool
    time_warp: WarpFunction | None
    screen_width: int
    screen_height: int
    child_width: int
    child_height: int
    delay: float
    st: float
    def __init__(
        self, delay: float, old: MultiBox, new: MultiBox, use_old: bool, time_warp: WarpFunction | None
    ) -> None: ...
    def render(self, width: float, height: float, st: float, at: float) -> renpy.display.render.Render: ...
    def child_placement(self, child) -> Placement: ...
    def get_placement(self) -> Placement: ...

def MoveTransition(
    delay,
    old_widget: Incomplete | None = None,
    new_widget: Incomplete | None = None,
    enter: renpy.display.transform.Transform | None = None,
    leave: renpy.display.transform.Transform | None = None,
    old: bool = False,
    layers: list[str] = ["master"],
    time_warp: WarpFunction | None = None,
    enter_time_warp: WarpFunction | None = None,
    leave_time_warp: WarpFunction | None = None,
) -> Incomplete: ...
