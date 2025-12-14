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
from renpy.display.render import render as render

class Transition(renpy.display.displayable.Displayable):
    new_widget: renpy.display.displayable.Displayable | None
    old_widget: renpy.display.displayable.Displayable | None
    delay: Incomplete
    events: bool
    def __init__(self, delay, **properties) -> None: ...
    def event(self, ev, x, y, st): ...
    def visit(self): ...
    def get_placement(self): ...

def null_render(d, width, height, st, at): ...

class NoTransition(Transition):
    old_widget: Incomplete
    new_widget: Incomplete
    events: bool
    def __init__(self, delay, old_widget=None, new_widget=None, **properties) -> None: ...
    def render(self, width, height, st, at): ...

class MultipleTransition(Transition):
    transitions: Incomplete
    screens: Incomplete
    new_widget: Incomplete
    events: bool
    def __init__(self, args, old_widget=None, new_widget=None, **properties) -> None: ...
    def visit(self): ...
    def event(self, ev, x, y, st): ...
    def render(self, width, height, st, at): ...

def Fade(
    out_time, hold_time, in_time, old_widget=None, new_widget=None, color=None, widget=None, alpha: bool = False
): ...

class Pixellate(Transition):
    time: Incomplete
    steps: Incomplete
    old_widget: Incomplete
    new_widget: Incomplete
    events: bool
    quantum: Incomplete
    def __init__(self, time, steps, old_widget=None, new_widget=None, **properties) -> None: ...
    def render(self, width, height, st, at): ...

class Dissolve(Transition):
    __version__: int
    alpha: bool
    def after_upgrade(self, version) -> None: ...
    time_warp: Incomplete
    time: Incomplete
    old_widget: Incomplete
    new_widget: Incomplete
    events: bool
    def __init__(
        self, time, old_widget=None, new_widget=None, alpha: bool = False, time_warp=None, **properties
    ) -> None: ...
    def render(self, width, height, st, at): ...

class ImageDissolve(Transition):
    __version__: int
    alpha: bool
    def after_upgrade(self, version) -> None: ...
    time_warp: Incomplete
    old_widget: Incomplete
    new_widget: Incomplete
    events: bool
    image: Incomplete
    ramplen: Incomplete
    def __init__(
        self,
        image,
        time,
        ramplen: int = 8,
        ramptype: str = "linear",
        ramp=None,
        reverse: bool = False,
        alpha: bool = False,
        old_widget=None,
        new_widget=None,
        time_warp=None,
        **properties,
    ) -> None: ...
    def visit(self): ...
    def render(self, width, height, st, at): ...

class AlphaDissolve(Transition):
    mipmap: Incomplete
    control: Incomplete
    old_widget: Incomplete
    new_widget: Incomplete
    events: bool
    alpha: Incomplete
    reverse: Incomplete
    def __init__(
        self,
        control,
        delay: float = 0.0,
        old_widget=None,
        new_widget=None,
        alpha: bool = False,
        reverse: bool = False,
        **properties,
    ) -> None: ...
    def visit(self): ...
    def render(self, width, height, st, at): ...

def interpolate_tuple(t0, t1, time, scales): ...

class CropMove(Transition):
    time: Incomplete
    delay: Incomplete
    startpos: Incomplete
    endpos: Incomplete
    startcrop: Incomplete
    endcrop: Incomplete
    topnew: Incomplete
    old_widget: Incomplete
    new_widget: Incomplete
    events: bool
    bottom: Incomplete
    top: Incomplete
    def __init__(
        self,
        time,
        mode: str = "slideright",
        startcrop=(0.0, 0.0, 0.0, 1.0),
        startpos=(0.0, 0.0),
        endcrop=(0.0, 0.0, 1.0, 1.0),
        endpos=(0.0, 0.0),
        topnew: bool = True,
        old_widget=None,
        new_widget=None,
        **properties,
    ) -> None: ...
    def render(self, width, height, st, at): ...

class PushMove(Transition):
    time: Incomplete
    new_startpos: Incomplete
    new_startcrop: Incomplete
    new_endpos: Incomplete
    new_endcrop: Incomplete
    old_endpos: Incomplete
    old_endcrop: Incomplete
    old_startpos: Incomplete
    old_startcrop: Incomplete
    delay: Incomplete
    old_widget: Incomplete
    new_widget: Incomplete
    events: bool
    def __init__(self, time, mode: str = "pushright", old_widget=None, new_widget=None, **properties) -> None: ...
    def render(self, width, height, st, at): ...

def ComposeTransition(trans, before=None, after=None, new_widget=None, old_widget=None): ...
def SubTransition(rect, trans, old_widget=None, new_widget=None, **properties): ...
