from _typeshed import Incomplete

from renpy.display.layout import Container as Container
from renpy.display.render import render as render
from renpy.display.transform import (
    ATLTransform as ATLTransform,
    Proxy as Proxy,
    Transform as Transform,
    TransformState as TransformState,
    null as null,
)

class Motion(Container):
    function: Incomplete
    period: Incomplete
    repeat: Incomplete
    bounce: Incomplete
    delay: Incomplete
    anim_timebase: Incomplete
    time_warp: Incomplete
    add_sizes: Incomplete
    position: Incomplete
    def __init__(
        self,
        function,
        period,
        child=None,
        new_widget=None,
        old_widget=None,
        repeat: bool = False,
        bounce: bool = False,
        delay=None,
        anim_timebase: bool = False,
        tag_start=None,
        time_warp=None,
        add_sizes: bool = False,
        style: str = "motion",
        **properties,
    ) -> None: ...
    def update_position(self, t, sizes) -> None: ...
    def get_placement(self): ...
    offsets: Incomplete
    def render(self, width, height, st, at): ...

class Interpolate:
    anchors: Incomplete
    start: Incomplete
    end: Incomplete
    def __init__(self, start, end) -> None: ...
    def __call__(self, t, sizes=(None, None, None, None)): ...

def Pan(
    startpos,
    endpos,
    time,
    child=None,
    repeat: bool = False,
    bounce: bool = False,
    anim_timebase: bool = False,
    style: str = "motion",
    time_warp=None,
    **properties,
): ...
def Move(
    startpos,
    endpos,
    time,
    child=None,
    repeat: bool = False,
    bounce: bool = False,
    anim_timebase: bool = False,
    style: str = "motion",
    time_warp=None,
    **properties,
): ...

class Revolver:
    start: Incomplete
    end: Incomplete
    around: Incomplete
    cor: Incomplete
    pos: Incomplete
    child: Incomplete
    def __init__(self, start, end, child, around=(0.5, 0.5), cor=(0.5, 0.5), pos=None) -> None: ...
    def __call__(self, t, rect): ...

def Revolve(start, end, time, child, around=(0.5, 0.5), cor=(0.5, 0.5), pos=None, **properties): ...
def zoom_render(crend, x, y, w, h, zw, zh, bilinear): ...

class ZoomCommon(renpy.display.displayable.Displayable):
    time: Incomplete
    child: Incomplete
    repeat: Incomplete
    after_child: Incomplete
    time_warp: Incomplete
    bilinear: Incomplete
    opaque: Incomplete
    anim_timebase: Incomplete
    def __init__(
        self,
        time,
        child,
        end_identity: bool = False,
        after_child=None,
        time_warp=None,
        bilinear: bool = True,
        opaque: bool = True,
        anim_timebase: bool = False,
        repeat: bool = False,
        style: str = "motion",
        **properties,
    ) -> None: ...
    def visit(self): ...
    def zoom_rectangle(self, done: float, width: float, height: float) -> tuple[int, int, int, int, int, int]: ...
    done: Incomplete
    def render(self, width, height, st, at): ...
    def event(self, ev, x, y, st): ...

class Zoom(ZoomCommon):
    size: Incomplete
    start: Incomplete
    end: Incomplete
    def __init__(self, size, start, end, time, child, **properties) -> None: ...
    def zoom_rectangle(self, done, width, height): ...

class FactorZoom(ZoomCommon):
    start: Incomplete
    end: Incomplete
    def __init__(self, start, end, time, child, **properties) -> None: ...
    def zoom_rectangle(self, done, width, height): ...

class SizeZoom(ZoomCommon):
    start: Incomplete
    end: Incomplete
    def __init__(self, start, end, time, child, **properties) -> None: ...
    def zoom_rectangle(self, done, width, height): ...

class RotoZoom(renpy.display.displayable.Displayable):
    transform: Incomplete
    rot_start: Incomplete
    rot_end: Incomplete
    rot_delay: Incomplete
    zoom_start: Incomplete
    zoom_end: Incomplete
    zoom_delay: Incomplete
    child: Incomplete
    rot_repeat: Incomplete
    zoom_repeat: Incomplete
    rot_bounce: Incomplete
    zoom_bounce: Incomplete
    rot_anim_timebase: Incomplete
    zoom_anim_timebase: Incomplete
    rot_time_warp: Incomplete
    zoom_time_warp: Incomplete
    opaque: Incomplete
    def __init__(
        self,
        rot_start,
        rot_end,
        rot_delay,
        zoom_start,
        zoom_end,
        zoom_delay,
        child,
        rot_repeat: bool = False,
        zoom_repeat: bool = False,
        rot_bounce: bool = False,
        zoom_bounce: bool = False,
        rot_anim_timebase: bool = False,
        zoom_anim_timebase: bool = False,
        rot_time_warp=None,
        zoom_time_warp=None,
        opaque: bool = False,
        style: str = "motion",
        **properties,
    ) -> None: ...
    def visit(self): ...
    def render(self, width, height, st, at): ...
