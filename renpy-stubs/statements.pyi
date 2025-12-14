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

registry: Incomplete
parsers: Incomplete

def register(
    name,
    parse=None,
    lint=None,
    execute=None,
    predict=None,
    next=None,
    scry=None,
    block: bool = False,
    init: bool = False,
    translatable: bool = False,
    execute_init=None,
    init_priority: int = 0,
    label=None,
    warp=None,
    translation_strings=None,
    force_begin_rollback: bool = False,
    post_execute=None,
    post_label=None,
    predict_all: bool = True,
    predict_next=None,
    execute_default=None,
    reachable=None,
): ...
def parse(node, line, subblock): ...
def call(method, parsed, *args, **kwargs): ...
def get(key, parsed): ...
def get_name(parsed): ...
