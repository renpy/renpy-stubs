import renpy
import renpy.sl2.slast as slast
from renpy.ast import NodeLocation as NodeLocation
from renpy.lexer import Lexer as Lexer
from renpy.object import Sentinel as Sentinel
from renpy.styledata.stylesets import proxy_properties as proxy_properties
from typing import Any, Callable, Iterable, Literal, Self

type ParserAddType = "Positional | Keyword | Style | PrefixStyle | Parser | Sequence[Positional | Keyword | Style | PrefixStyle | Parser]"
STYLE_PREFIXES: list[str]
parser: Parser | None
statements: dict[str, Parser]
all_child_statements: list[Parser]
childbearing_statements: set[Parser]

class Positional:
    name: str
    def __init__(self, name: str) -> None: ...

properties: dict[tuple[str, bool], set[str]]

class Keyword:
    name: str
    def __init__(self, name: str) -> None: ...

class Style:
    name: str
    def __init__(self, name: str) -> None: ...

class PrefixStyle:
    prefix: str
    name: str
    def __init__(self, prefix: str, name: str) -> None: ...

incompatible_props: dict[str, frozenset[str]]

def update_incompatible_props(prefix: str, prop: str) -> None: ...
def check_incompatible_props(new: str, olds: Iterable[str]) -> str | Literal[False]: ...

class Parser:
    nchildren: str
    name: str
    positional: list[Positional]
    keyword: dict[str, Keyword]
    children: dict[str, Parser]
    variable: bool
    def __init__(self, name: str, child_statement: bool = True) -> None: ...
    def __repr__(self) -> str: ...
    def add(self, i: ParserAddType) -> None: ...
    def parse_statement(
        self, loc: NodeLocation, l: Lexer, layout_mode: bool = False, keyword: bool = True
    ) -> slast.SLNode | None: ...
    def parse_layout(self, loc: NodeLocation, l: Lexer, parent: Parser, keyword: bool) -> slast.SLNode: ...
    def parse(self, loc: NodeLocation, l: Lexer, parent: Parser, keyword: bool) -> slast.SLNode: ...
    def parse_contents(
        self,
        l: Lexer,
        target: slast.SLBlock,
        layout_mode: bool = False,
        can_has: bool = False,
        can_tag: bool = False,
        block_only: bool = False,
        keyword: bool = True,
        docstring: bool = False,
    ) -> None: ...
    def add_positional(self, name: str) -> Self: ...
    def add_property(self, name: str) -> Self: ...
    def add_style_property(self, name: str) -> Self: ...
    def add_prefix_style_property(self, prefix: str, name: str) -> Self: ...
    def add_property_group(self, group: str, prefix: str = "") -> Self: ...
    def copy_properties(self, name: str) -> Self: ...

def add(thing: ParserAddType) -> None: ...

many: renpy.object.Sentinel

def register_sl_displayable(*args, **kwargs) -> DisplayableParser: ...

class DisplayableParser(Parser):
    displayable: Callable[..., renpy.display.displayable.Displayable]
    nchildren: int | Sentinel
    style: str | None
    scope: bool
    pass_context: bool
    imagemap: bool
    hotspot: bool
    replaces: bool
    default_keywords: dict[str, Any]
    variable: bool
    unique: bool
    def __init__(
        self,
        name: str,
        displayable: Callable[..., renpy.display.displayable.Displayable],
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
    def parse_layout(self, loc: NodeLocation, l: Lexer, parent: Parser, keyword: bool) -> slast.SLDisplayable: ...
    def parse(
        self, loc: NodeLocation, l: Lexer, parent: Parser, keyword: bool, layout_mode: bool = False
    ) -> slast.SLDisplayable: ...

class IfParser(Parser):
    node_type: type[slast.SLIf | slast.SLShowIf]
    parent_contents: bool
    def __init__(self, name: str, node_type: type[slast.SLIf | slast.SLShowIf], parent_contents: bool) -> None: ...
    def parse(self, loc: NodeLocation, l: Lexer, parent: Parser, keyword: bool) -> slast.SLNode: ...

if_statement: IfParser

class ForParser(Parser):
    def __init__(self, name: str) -> None: ...
    def name_or_tuple_pattern(self, l: Lexer) -> str | None: ...
    def parse(self, loc: NodeLocation, l: Lexer, parent: Parser, keyword: bool) -> slast.SLFor: ...

for_parser: ForParser

class BreakParser(Parser):
    def parse(self, loc: NodeLocation, l: Lexer, parent: Parser, keyword: bool) -> slast.SLBreak: ...

class ContinueParser(Parser):
    def parse(self, loc: NodeLocation, l: Lexer, parent: Parser, keyword: bool) -> slast.SLContinue: ...

class OneLinePythonParser(Parser):
    def parse(self, loc: NodeLocation, l: Lexer, parent: Parser, keyword: bool) -> slast.SLPython: ...

class MultiLinePythonParser(Parser):
    def parse(self, loc: NodeLocation, l: Lexer, parent: Parser, keyword: bool) -> slast.SLPython: ...

class PassParser(Parser):
    def parse(self, loc: NodeLocation, l: Lexer, parent: Parser, keyword: bool) -> slast.SLPass: ...

pass_statement: PassParser

class DefaultParser(Parser):
    def parse(self, loc: NodeLocation, l: Lexer, parent: Parser, keyword: bool) -> slast.SLDefault: ...

class UseParser(Parser):
    def __init__(self, name: str) -> None: ...
    def parse(self, loc: NodeLocation, l: Lexer, parent: Parser, keyword: bool) -> slast.SLUse: ...

class TranscludeParser(Parser):
    def parse(self, loc: NodeLocation, l: Lexer, parent: Parser, keyword: bool) -> slast.SLTransclude: ...

class CustomParser(Parser):
    nchildren: int | Sentinel
    screen: str
    variable: bool
    def __init__(
        self, name: str, children: int | Literal["many"] | Sentinel = "many", screen: str | None = None
    ) -> None: ...
    def parse(self, loc: NodeLocation, l: Lexer, parent: Parser, keyword: bool) -> slast.SLCustomUse: ...

class ScreenParser(Parser):
    def __init__(self) -> None: ...
    def parse(
        self, loc: NodeLocation, l: Lexer, parent: Parser, name: str = "_name", keyword: bool = True
    ) -> slast.SLScreen: ...

screen_parser: ScreenParser

def init() -> None: ...
def parse_screen(l: Lexer, loc: NodeLocation) -> slast.SLScreen: ...
