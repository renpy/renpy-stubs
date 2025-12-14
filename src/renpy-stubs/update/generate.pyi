from . import common as common
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

class BlockGenerator:
    lock: Incomplete
    targetdir: Incomplete
    seen_hashes: Incomplete
    max_rpu_size: Incomplete
    blocks: Incomplete
    filelist: Incomplete
    segments: Incomplete
    new_rpu: Incomplete
    def __init__(self, targetdir, max_rpu_size=...) -> None: ...
    def path(self, name): ...
    def open_new_rpu(self) -> None: ...
    def close_new_rpu(self) -> None: ...
    def generate_segment(self, f, seg) -> None: ...
    def generate(self, name, filelist, progress=None): ...
