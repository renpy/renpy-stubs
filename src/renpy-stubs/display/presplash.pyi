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

window: Incomplete
progress_bar: Incomplete
start_time: Incomplete

class ProgressBar:
    foreground: Incomplete
    background: Incomplete
    def __init__(self, foreground, background) -> None: ...
    def convert_alpha(self, surface=None) -> None: ...
    def get_size(self): ...
    def get_at(self, pos): ...
    def draw(self, target, done) -> None: ...

def find_file(base_name, root): ...
def start(basedir, gamedir) -> None: ...

last_pump_time: int
pump_count: int
pump_clock: int
pump_total: int

def pump_window() -> None: ...

done: bool

def end() -> None: ...
def sleep() -> None: ...

progress_kind: Incomplete

def progress(kind, done, total) -> None: ...
