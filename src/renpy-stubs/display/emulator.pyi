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

emulator: Incomplete
overlay: Incomplete
ios: bool

def null_emulator(ev, x, y): ...

TOUCH_KEYS: Incomplete

def touch_emulator(ev, x, y): ...

TV_KEYS: Incomplete

def tv_emulator(ev, x, y): ...

keyboard: Incomplete
null: Incomplete

def dynamic_keyboard(st, at): ...
def init_emulator() -> None: ...
def early_init_emulator() -> None: ...
