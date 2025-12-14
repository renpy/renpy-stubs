from _typeshed import Incomplete
from collections.abc import Generator
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

update_translations: Incomplete
flags: Incomplete
formatter: Incomplete
SIMPLE_NAME: Incomplete

def interpolate(s, scope): ...
def parse(s) -> Generator[Incomplete]: ...
def convert(value, conv, scope): ...
def substitute(s, scope=None, force: bool = False, translate: bool = True): ...
def ___(s): ...
