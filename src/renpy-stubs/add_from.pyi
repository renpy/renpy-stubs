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

missing: Incomplete

def report_missing(target, filename, loc) -> None: ...

new_labels: Incomplete

def generate_label(target): ...
def process_file(fn) -> None: ...
def clear() -> None: ...
def add_from(): ...
