from _typeshed import Incomplete as Incomplete
from renpy.object import Sentinel as Sentinel
from renpy.styledata.stylesets import proxy_properties as proxy_properties
from typing import Any, Callable, Literal

STYLE_PREFIXES: Incomplete
parser: Incomplete
statements: Incomplete
all_child_statements: Incomplete
childbearing_statements: Incomplete

class Positional:
    name: Incomplete
    def __init__(self, name: Incomplete) -> None: ...

properties: Incomplete

class Keyword:
    name: Incomplete
    def __init__(self, name: Incomplete) -> None: ...

class Style:
    name: Incomplete
    def __init__(self, name: Incomplete) -> None: ...

class PrefixStyle:
    prefix: Incomplete
    name: Incomplete
    def __init__(self, prefix: Incomplete, name: Incomplete) -> None: ...

incompatible_props: Incomplete

def update_incompatible_props(prefix: Incomplete, prop: Incomplete) -> None: ...
def check_incompatible_props(new: Incomplete, olds: Incomplete) -> Incomplete: ...

class Parser:
    nchildren: str
    name: Incomplete
    positional: Incomplete
    keyword: Incomplete
    children: Incomplete
    variable: bool
    def __init__(self, name: Incomplete, child_statement: bool = True) -> None: ...
    def add(self, i: Incomplete) -> None: ...
    def parse_statement(
        self, loc: Incomplete, l: Incomplete, layout_mode: bool = False, keyword: bool = True
    ) -> Incomplete: ...
    def parse_layout(self, loc: Incomplete, l: Incomplete, parent: Incomplete, keyword: Incomplete) -> None: ...
    def parse(self, loc: Incomplete, l: Incomplete, parent: Incomplete, keyword: Incomplete) -> None: ...
    def parse_contents(
        self,
        l: Incomplete,
        target: Incomplete,
        layout_mode: bool = False,
        can_has: bool = False,
        can_tag: bool = False,
        block_only: bool = False,
        keyword: bool = True,
        docstring: bool = False,
    ) -> Incomplete: ...
    def add_positional(self, name: Incomplete) -> Incomplete: ...
    def add_property(self, name: Incomplete) -> Incomplete: ...
    def add_style_property(self, name: Incomplete) -> Incomplete: ...
    def add_prefix_style_property(self, prefix: Incomplete, name: Incomplete) -> Incomplete: ...
    def add_property_group(self, group: Incomplete, prefix: str = "") -> Incomplete: ...
    def copy_properties(self, name: Incomplete) -> Incomplete: ...

def add(thing: Incomplete) -> None: ...

many: Incomplete

def register_sl_displayable(*args, **kwargs) -> Incomplete: ...

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
        nchildren: int | Literal["many"] | Sentinel = 0,
        scope: bool = False,
        pass_context: bool = False,
        imagemap: bool = False,
        replaces: bool = False,
        default_keywords: dict[str, Any] = {},
        hotspot: bool = False,
        default_properties: bool = True,
        unique: bool = False,
    ) -> None: ...
    def parse_layout(self, loc: Incomplete, l: Incomplete, parent: Incomplete, keyword: Incomplete) -> Incomplete: ...
    def parse(
        self, loc: Incomplete, l: Incomplete, parent: Incomplete, keyword: Incomplete, layout_mode: bool = False
    ) -> Incomplete: ...

class IfParser(Parser):
    node_type: Incomplete
    parent_contents: Incomplete
    def __init__(self, name: Incomplete, node_type: Incomplete, parent_contents: Incomplete) -> None: ...
    def parse(self, loc: Incomplete, l: Incomplete, parent: Incomplete, keyword: Incomplete) -> Incomplete: ...

if_statement: Incomplete

class ForParser(Parser):
    def __init__(self, name: Incomplete) -> None: ...
    def name_or_tuple_pattern(self, l: Incomplete) -> Incomplete: ...
    def parse(self, loc: Incomplete, l: Incomplete, parent: Incomplete, keyword: Incomplete) -> Incomplete: ...

for_parser: Incomplete

class BreakParser(Parser):
    def parse(self, loc: Incomplete, l: Incomplete, parent: Incomplete, keyword: Incomplete) -> Incomplete: ...

class ContinueParser(Parser):
    def parse(self, loc: Incomplete, l: Incomplete, parent: Incomplete, keyword: Incomplete) -> Incomplete: ...

class OneLinePythonParser(Parser):
    def parse(self, loc: Incomplete, l: Incomplete, parent: Incomplete, keyword: Incomplete) -> Incomplete: ...

class MultiLinePythonParser(Parser):
    def parse(self, loc: Incomplete, l: Incomplete, parent: Incomplete, keyword: Incomplete) -> Incomplete: ...

class PassParser(Parser):
    def parse(self, loc: Incomplete, l: Incomplete, parent: Incomplete, keyword: Incomplete) -> Incomplete: ...

pass_statement: Incomplete

class DefaultParser(Parser):
    def parse(self, loc: Incomplete, l: Incomplete, parent: Incomplete, keyword: Incomplete) -> Incomplete: ...

class UseParser(Parser):
    def __init__(self, name: Incomplete) -> None: ...
    def parse(self, loc: Incomplete, l: Incomplete, parent: Incomplete, keyword: Incomplete) -> Incomplete: ...

class TranscludeParser(Parser):
    def parse(self, loc: Incomplete, l: Incomplete, parent: Incomplete, keyword: Incomplete) -> Incomplete: ...

class CustomParser(Parser):
    nchildren: Incomplete
    screen: Incomplete
    variable: bool
    def __init__(self, name: Incomplete, children: str = "many", screen: Incomplete = None) -> None: ...
    def parse(self, loc: Incomplete, l: Incomplete, parent: Incomplete, keyword: Incomplete) -> Incomplete: ...

class ScreenParser(Parser):
    def __init__(self) -> None: ...
    def parse(
        self, loc: Incomplete, l: Incomplete, parent: Incomplete, name: str = "_name", keyword: bool = True
    ) -> Incomplete: ...

screen_parser: Incomplete

def init() -> None: ...
def parse_screen(l: Incomplete, loc: Incomplete) -> Incomplete: ...
