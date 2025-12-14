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

definitions: Incomplete
transforms: Incomplete
screens: Incomplete
file_exists_cache: Incomplete

def file_exists(fn): ...

completed_dump: bool

def dump(error): ...
