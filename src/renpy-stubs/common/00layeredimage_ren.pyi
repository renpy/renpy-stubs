import renpy
from collections import defaultdict
from collections.abc import Iterable
from renpy import config as config
from renpy.atl import RawBlock as RawBlock, parse_atl as parse_atl
from renpy.defaultstore import At as At
from renpy.display.displayable import Displayable as Displayable, DisplayableArguments as DisplayableArguments
from renpy.display.layout import ConditionSwitch as ConditionSwitch, Fixed as Fixed, Null as Null, Position as Position
from renpy.display.transform import ATLTransform as ATLTransform, Transform as Transform
from renpy.lexer import Lexer as Lexer
from renpy.object import Object as Object
from renpy.text.text import Text as Text
from renpy.types import DisplayableLike as DisplayableLike
from typing import Any, Callable, Container, Literal, Protocol, Self, overload

python_object = object
_constant: bool
type Imageable = RawBlock | str | None
type AttributeFunction = Callable[[set[str]], Iterable[str]]

class FormatFunction(Protocol):
    def __call__(
        self,
        what: str,
        name: str | None,
        group: str | None,
        variant: str | None,
        attribute: str | None,
        image: str | Displayable | None,
        image_format: str | None,
    ) -> str | Displayable: ...

ATL_PROPERTIES: frozenset[str]
FIXED_PROPERTIES: frozenset[str]
BASE_PROPERTIES: frozenset[str]
LAYER_PROPERTIES: frozenset[str]
ATTRIBUTE_PROPERTIES: frozenset[str]
GROUP_BLOCK_PROPERTIES: frozenset[str]
GROUP_INLINE_PROPERTIES: frozenset[str]
CONDITION_PROPERTIES: frozenset[str]
ALWAYS_PROPERTIES: frozenset[str]
predict_all: bool | None

@overload
def format_function(
    what: str,
    name: str | None,
    group: str | None,
    variant: str | None,
    attribute: str | None,
    image: str | None,
    image_format: str | None,
    **kwargs,
) -> str: ...
@overload
def format_function(
    what: str,
    name: str | None,
    group: str | None,
    variant: str | None,
    attribute: str | None,
    image: Displayable,
    image_format: str | None,
    **kwargs,
) -> Displayable: ...
@overload
def resolve_image(img: None) -> None: ...
@overload
def resolve_image(img: RawBlock) -> ATLTransform: ...
@overload
def resolve_image(img: str) -> Displayable: ...
def resolve_at(at: RawBlock | Transform | Iterable[Transform]) -> tuple[Transform, ...]: ...

class When(python_object):
    __slots__: str | Iterable[str]
    def __init__(self) -> None: ...
    def check(self, attributes: Iterable[str]) -> bool: ...
    @staticmethod
    def parse(l: Lexer) -> When: ...

class WhenOr(When):
    __slots__: str | Iterable[str]
    left: When
    right: When
    def __init__(self, left: When, right: When, /) -> None: ...
    def check(self, attributes: Iterable[str]) -> bool: ...
    @staticmethod
    def parse(l: Lexer) -> When: ...

class WhenAnd(When):
    __slots__: str | Iterable[str]
    left: When
    right: When
    def __init__(self, left: When, right: When, /) -> None: ...
    def check(self, attributes: Iterable[str]) -> bool: ...
    @staticmethod
    def parse(l: Lexer) -> When: ...

class WhenNot(When):
    __slots__: str | Iterable[str]
    when: When
    def __init__(self, when: When, /) -> None: ...
    def check(self, attributes: Iterable[str]) -> bool: ...
    @staticmethod
    def parse(l: Lexer) -> When: ...

class WhenAttribute(When):
    __slots__: str | Iterable[str]
    attribute: str
    def __init__(self, attribute: str, /) -> None: ...
    def check(self, attributes: Iterable[str]) -> bool: ...
    @staticmethod
    def parse(l: Lexer) -> When: ...

class Layer:
    group_args: dict[str, Any]
    at: tuple[Transform, ...]
    when: When | None
    if_all: list[str]
    if_any: list[str]
    if_not: list[str]
    transform_args: dict[str, Any]
    def __init__(
        self,
        if_all: str | Iterable[str] = [],
        if_any: str | Iterable[str] = [],
        if_not: str | Iterable[str] = [],
        at: Transform | Iterable[Transform] = (),
        group_args: dict[str, Any] = {},
        *,
        when: When | str | None = None,
        **kwargs,
    ) -> None: ...
    def check(self, attributes: Iterable[str]) -> bool: ...
    def wrap(self, d: DisplayableLike) -> Displayable: ...
    def apply_format(self, li: LayeredImage, /): ...
    def get_displayable(self, attributes: Iterable[str]) -> Displayable | None: ...

class Attribute(Layer):
    group: str | None
    raw_attribute: str
    attribute: str
    image: Displayable | None
    default: bool
    variant: str | None
    def __init__(
        self,
        group: str | None,
        attribute: str,
        image: Displayable | None = None,
        default: bool = False,
        *,
        prefix: str | None = None,
        variant: str | None = None,
        **kwargs,
    ) -> None: ...
    def apply_format(self, li: LayeredImage): ...
    def get_displayable(self, attributes: Iterable[str]) -> Displayable | None: ...

class Condition(Layer):
    at: renpy.display.scenelists.AtList
    condition: str | None
    image: Displayable | None
    def __init__(self, condition: str | None, image: Displayable | None, **kwargs) -> None: ...
    def apply_format(self, li: LayeredImage): ...
    def get_displayable(self, attributes: Iterable[str]) -> Position | None: ...

class ConditionGroup(Layer):
    conditions: Iterable[Condition]
    def __init__(self, conditions: Iterable[Condition] = ()) -> None: ...
    def apply_format(self, li: LayeredImage): ...
    def get_displayable(self, attributes: Iterable[str]) -> Position: ...

class Always(Layer):
    image: Displayable | None
    def __init__(self, image: Displayable | None, **kwargs) -> None: ...
    def apply_format(self, li: LayeredImage): ...
    def get_displayable(self, attributes: Iterable[str]) -> Displayable | None: ...

class LayeredImage:
    attribute_function: AttributeFunction | None
    transform_args: dict[str, Any]
    offer_screen: bool | None
    name: str | None
    image_format: str | None
    format_function: FormatFunction
    attributes: list[Attribute]
    layers: list[Layer]
    attribute_to_groups: defaultdict[str, set[str]]
    group_to_attributes: defaultdict[str, set[str]]
    at: tuple[Transform, ...]
    fixed_args: dict[str, Any]
    def __init__(
        self,
        attributes: Iterable[Layer | Displayable],
        at: RawBlock | Transform | list[Transform] = [],
        name: str | None = None,
        image_format: str | None = None,
        format_function: FormatFunction = ...,
        attribute_function: AttributeFunction | None = None,
        offer_screen: bool | None = None,
        **kwargs,
    ) -> None: ...
    def format(
        self,
        what: str,
        attribute: str | None = None,
        group: str | None = None,
        variant: str | None = None,
        image: Displayable | None = None,
    ) -> str | Displayable: ...
    def add(self, a: Layer | Displayable) -> None: ...
    def get_banned(self, attributes: Iterable[str]) -> set[str]: ...
    def _duplicate(self, args: DisplayableArguments | None = None) -> Self: ...
    def _list_attributes(self, tag: str, attributes: Iterable[str]) -> list[str]: ...
    def _choose_attributes(
        self, tag: str, required: Iterable[str], optional: Iterable[str] | None
    ) -> tuple[str, ...] | None: ...

def parse_property(
    l: Lexer, final_properties: dict[str, Any], expr_properties: dict[str, str], names: Container[str]
) -> Literal[0] | Literal[1] | Literal[2]: ...
def parse_displayable(l: Lexer) -> Imageable: ...

class RawAttribute(renpy.object.Object):
    __version__: int
    expr_properties: dict[str, str]
    final_properties: dict[str, Any]
    def after_upgrade(self, version: int) -> None: ...
    name: str
    image: Imageable
    def __init__(self, name: str) -> None: ...
    def execute(self, group_name: str | None = None, **group_properties) -> list[Attribute]: ...

def parse_attribute(l: Lexer) -> RawAttribute: ...

class RawAttributeGroup(renpy.object.Object):
    __version__: int
    expr_properties: dict[str, str]
    final_properties: dict[str, Any]
    group_name: str | None
    li_name: str
    def after_upgrade(self, version: int) -> None: ...
    children: list[RawAttribute]
    def __init__(self, li_name: str, group_name: str | None) -> None: ...
    def execute(self) -> list[Attribute]: ...

def parse_group(l: Lexer, li_name: str) -> RawAttributeGroup: ...

class RawCondition(renpy.object.Object):
    __version__: int
    expr_properties: dict[str, str]
    final_properties: dict[str, Any]
    def after_upgrade(self, version: int) -> None: ...
    condition: str | None
    image: Imageable
    def __init__(self, condition: str | None) -> None: ...
    def execute(self) -> list[Condition]: ...

def parse_condition(l: Lexer, need_expr: bool) -> RawCondition: ...

class RawConditionGroup:
    conditions: Iterable[RawCondition]
    def __init__(self, conditions: Iterable[RawCondition] = ()) -> None: ...
    def execute(self) -> list[ConditionGroup]: ...

def parse_conditions(l: Lexer) -> RawConditionGroup: ...

class RawAlways(renpy.object.Object):
    __version__: int
    expr_properties: dict[str, str]
    final_properties: dict[str, Any]
    def after_upgrade(self, version: int) -> None: ...
    image: Imageable
    def __init__(self) -> None: ...
    def execute(self) -> list[Always]: ...

def parse_always(l: Lexer) -> RawAlways: ...

class RawLayeredImage(renpy.object.Object):
    __version__: int
    expr_properties: dict[str, str]
    final_properties: dict[str, Any]
    def after_upgrade(self, version: int) -> None: ...
    name: str
    children: list[RawAlways | RawAttribute | RawAttributeGroup | RawConditionGroup]
    def __init__(self, name: str) -> None: ...
    def execute(self) -> None: ...

def execute_layeredimage(rai: RawLayeredImage) -> None: ...
def parse_layeredimage(l: Lexer) -> RawLayeredImage: ...
def lint_layeredimage(rli: RawLayeredImage) -> None: ...

class LayeredImageProxy:
    name: str
    transform: list[Transform]
    def __init__(self, name: str, transform: Transform | list[Transform] | None = None) -> None: ...
    @property
    def image(self) -> LayeredImage: ...
    def _duplicate(self, args: DisplayableArguments | None = None) -> Self: ...
    def filter_attributes(self, attributes: Iterable[str] | None) -> tuple[str, ...] | None: ...
    def _choose_attributes(
        self, tag: str, attributes: Iterable[str], optional: Iterable[str] | None
    ) -> tuple[str, ...] | None: ...
    def _list_attributes(self, tag: str, attributes: Iterable[str]) -> list[str] | None: ...
