from _typeshed import Incomplete as Incomplete

registry: Incomplete
parsers: Incomplete

def register(
    name: Incomplete,
    parse: Incomplete = None,
    lint: Incomplete = None,
    execute: Incomplete = None,
    predict: Incomplete = None,
    next: Incomplete = None,
    scry: Incomplete = None,
    block: bool = False,
    init: bool = False,
    translatable: bool = False,
    execute_init: Incomplete = None,
    init_priority: int = 0,
    label: Incomplete = None,
    warp: Incomplete = None,
    translation_strings: Incomplete = None,
    force_begin_rollback: bool = False,
    post_execute: Incomplete = None,
    post_label: Incomplete = None,
    predict_all: bool = True,
    predict_next: Incomplete = None,
    execute_default: Incomplete = None,
    reachable: Incomplete = None,
) -> Incomplete: ...
def parse(node: Incomplete, line: Incomplete, subblock: Incomplete) -> Incomplete: ...
def call(method: Incomplete, parsed: Incomplete, *args: Incomplete, **kwargs: Incomplete) -> Incomplete: ...
def get(key: Incomplete, parsed: Incomplete) -> Incomplete: ...
def get_name(parsed: Incomplete) -> Incomplete: ...
