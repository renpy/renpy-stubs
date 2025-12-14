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

fpl: Incomplete
DEPTH_LEVELS: int
running: bool

def clear() -> None: ...
def log(depth, event, *args) -> None: ...
def PPP(event, *args) -> None: ...
def analyze() -> None: ...
