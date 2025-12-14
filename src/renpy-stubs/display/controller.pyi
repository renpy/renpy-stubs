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
from renpy.pygame import (
    CONTROLLERAXISMOTION as CONTROLLERAXISMOTION,
    CONTROLLERBUTTONDOWN as CONTROLLERBUTTONDOWN,
    CONTROLLERBUTTONUP as CONTROLLERBUTTONUP,
    CONTROLLERDEVICEADDED as CONTROLLERDEVICEADDED,
    CONTROLLERDEVICEREMOVED as CONTROLLERDEVICEREMOVED,
)
from renpy.pygame.controller import (
    Controller as Controller,
    get_string_for_axis as get_string_for_axis,
    get_string_for_button as get_string_for_button,
)

def load_mappings() -> None: ...
def init() -> None: ...

controllers: Incomplete
axis_positions: Incomplete
THRESHOLD: Incomplete
ZERO_THRESHOLD: int
ignore: bool

def post_event(control, state, repeat) -> None: ...
def exists(): ...
def quit(index) -> None: ...
def start(index) -> None: ...

class PadEvent:
    control: Incomplete
    state: Incomplete
    repeat_time: int
    def __init__(self, control) -> None: ...
    def event(self, state) -> None: ...
    def repeat(self) -> None: ...

pad_events: Incomplete

def controller_event(control, state) -> None: ...
def periodic() -> None: ...
def event(ev): ...
