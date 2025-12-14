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

DEFERRED_UPDATE_FILE: str
DELETED_DIRECTORY: str
first_deferred_delete: bool

def delete(fn: str): ...
def process_deferred_line(l): ...
def process_deferred(): ...
def process_deleted() -> None: ...
def defer_rename(fn) -> None: ...
def defer_delete(fn) -> None: ...
def init(): ...
