import renpy
from _typeshed import Incomplete as Incomplete
from renpy.display.displayable import Displayable as Displayable

def position(d): ...
def offsets(d): ...
def MoveFactory(pos1, pos2, delay, d, **kwargs): ...
def default_enter_factory(pos, delay, d, **kwargs): ...
def default_leave_factory(pos, delay, d, **kwargs) -> None: ...
def MoveIn(pos, pos1, delay, d, **kwargs): ...
def MoveOut(pos, pos1, delay, d, **kwargs): ...
def ZoomInOut(start, end, pos, delay, d, **kwargs): ...
def RevolveInOut(start, end, pos, delay, d, **kwargs): ...
def OldMoveTransition(
    delay,
    old_widget=None,
    new_widget=None,
    factory=None,
    enter_factory=None,
    leave_factory=None,
    old: bool = False,
    layers=["master"],
): ...

class MoveInterpolate(renpy.display.displayable.Displayable):
    old: Incomplete
    new: Incomplete
    use_old: Incomplete
    time_warp: Incomplete
    screen_width: int
    screen_height: int
    child_width: int
    child_height: int
    delay: int | float
    st: int
    def __init__(self, delay, old, new, use_old, time_warp) -> None: ...
    def render(self, width, height, st, at): ...
    def child_placement(self, child): ...
    def get_placement(self): ...

def MoveTransition(
    delay,
    old_widget=None,
    new_widget=None,
    enter=None,
    leave=None,
    old: bool = False,
    layers=["master"],
    time_warp=None,
    enter_time_warp=None,
    leave_time_warp=None,
): ...
