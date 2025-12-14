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

memory_log: Incomplete
constant_containers: Incomplete

def print_garbage(gen) -> None: ...
def write(s) -> None: ...
def cycle_finder(o, name): ...
def walk_memory(roots, seen=None): ...
def profile_memory_common(packages=["renpy", "store"], skip_constants: bool = False): ...
def profile_memory(fraction: float = 1.0, minimum: int = 0, skip_constants: bool = False) -> None: ...

old_usage: Incomplete
old_total: int

def diff_memory(update: bool = True, skip_constants: bool = False) -> None: ...
def profile_rollback() -> None: ...
def find_parents(cls) -> None: ...
