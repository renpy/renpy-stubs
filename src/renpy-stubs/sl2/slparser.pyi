import renpy
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
from renpy.styledata.stylesets import proxy_properties as proxy_properties
from typing import Any, Callable, Literal

STYLE_PREFIXES: Incomplete
parser: Incomplete
statements: Incomplete
all_child_statements: Incomplete
childbearing_statements: Incomplete

class Positional:
    name: Incomplete
    def __init__(self, name) -> None: ...

properties: Incomplete

class Keyword:
    name: Incomplete
    def __init__(self, name) -> None: ...

class Style:
    name: Incomplete
    def __init__(self, name) -> None: ...

class PrefixStyle:
    prefix: Incomplete
    name: Incomplete
    def __init__(self, prefix, name) -> None: ...

incompatible_props: Incomplete

def update_incompatible_props(prefix, prop) -> None: ...
def check_incompatible_props(new, olds): ...

class Parser:
    nchildren: str
    name: Incomplete
    positional: Incomplete
    keyword: Incomplete
    children: Incomplete
    variable: bool
    def __init__(self, name, child_statement: bool = True) -> None: ...
    def add(self, i) -> None: ...
    def parse_statement(self, loc, l, layout_mode: bool = False, keyword: bool = True): ...
    def parse_layout(self, loc, l, parent, keyword) -> None: ...
    def parse(self, loc, l, parent, keyword) -> None: ...
    def parse_contents(
        self,
        l,
        target,
        layout_mode: bool = False,
        can_has: bool = False,
        can_tag: bool = False,
        block_only: bool = False,
        keyword: bool = True,
        docstring: bool = False,
    ): ...
    def add_positional(self, name): ...
    def add_property(self, name): ...
    def add_style_property(self, name): ...
    def add_prefix_style_property(self, prefix, name): ...
    def add_property_group(self, group, prefix: str = ""): ...
    def copy_properties(self, name): ...

def add(thing) -> None: ...

many: Incomplete

def register_sl_displayable(*args, **kwargs): ...

class DisplayableParser(Parser):
    displayable: Incomplete
    nchildren: Incomplete
    style: Incomplete
    scope: Incomplete
    pass_context: Incomplete
    imagemap: Incomplete
    hotspot: Incomplete
    replaces: Incomplete
    default_keywords: Incomplete
    variable: bool
    unique: Incomplete
    def __init__(
        self,
        name: str,
        displayable: Callable,
        style: str | None,
        nchildren: int | Literal["many"] | renpy.object.Sentinel = 0,
        scope: bool = False,
        pass_context: bool = False,
        imagemap: bool = False,
        replaces: bool = False,
        default_keywords: dict[str, Any] = {},
        hotspot: bool = False,
        default_properties: bool = True,
        unique: bool = False,
    ) -> None: ...
    def parse_layout(self, loc, l, parent, keyword): ...
    def parse(self, loc, l, parent, keyword, layout_mode: bool = False): ...

class IfParser(Parser):
    node_type: Incomplete
    parent_contents: Incomplete
    def __init__(self, name, node_type, parent_contents) -> None: ...
    def parse(self, loc, l, parent, keyword): ...

if_statement: Incomplete

class ForParser(Parser):
    def __init__(self, name) -> None: ...
    def name_or_tuple_pattern(self, l): ...
    def parse(self, loc, l, parent, keyword): ...

for_parser: Incomplete

class BreakParser(Parser):
    def parse(self, loc, l, parent, keyword): ...

class ContinueParser(Parser):
    def parse(self, loc, l, parent, keyword): ...

class OneLinePythonParser(Parser):
    def parse(self, loc, l, parent, keyword): ...

class MultiLinePythonParser(Parser):
    def parse(self, loc, l, parent, keyword): ...

class PassParser(Parser):
    def parse(self, loc, l, parent, keyword): ...

pass_statement: Incomplete

class DefaultParser(Parser):
    def parse(self, loc, l, parent, keyword): ...

class UseParser(Parser):
    def __init__(self, name) -> None: ...
    def parse(self, loc, l, parent, keyword): ...

class TranscludeParser(Parser):
    def parse(self, loc, l, parent, keyword): ...

class CustomParser(Parser):
    nchildren: Incomplete
    screen: Incomplete
    variable: bool
    def __init__(self, name, children: str = "many", screen=None) -> None: ...
    def parse(self, loc, l, parent, keyword): ...

class ScreenParser(Parser):
    def __init__(self) -> None: ...
    def parse(self, loc, l, parent, name: str = "_name", keyword: bool = True): ...

screen_parser: Incomplete

def init() -> None: ...
def parse_screen(l, loc): ...
