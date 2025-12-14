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

DIRECTIONS: Incomplete

def dispatch_gesture(gesture) -> None: ...

class GestureRecognizer:
    x: Incomplete
    y: Incomplete
    def __init__(self) -> None: ...
    min_component: Incomplete
    min_stroke: Incomplete
    current_stroke: Incomplete
    stroke_length: int
    strokes: Incomplete
    def start(self, x, y) -> None: ...
    def take_point(self, x, y) -> None: ...
    def finish(self): ...
    def cancel(self) -> None: ...
    def event(self, ev, x, y): ...

recognizer: Incomplete
