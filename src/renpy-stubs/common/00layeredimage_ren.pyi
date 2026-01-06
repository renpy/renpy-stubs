import renpy
from _typeshed import Incomplete as Incomplete
from collections import defaultdict
from collections.abc import Iterable
from renpy.atl import RawBlock as RawBlock, parse_atl as parse_atl
from renpy.display.transform import ATLTransform as ATLTransform
from renpy.object import Object as Object
from store import Transform
from typing import Container, Literal

python_object = object
type Imageable = RawBlock | str | None
ATL_PROPERTIES: Incomplete
FIXED_PROPERTIES: Incomplete
BASE_PROPERTIES: Incomplete
LAYER_PROPERTIES: Incomplete
ATTRIBUTE_PROPERTIES: Incomplete
GROUP_BLOCK_PROPERTIES: Incomplete
GROUP_INLINE_PROPERTIES: Incomplete
CONDITION_PROPERTIES = LAYER_PROPERTIES
ALWAYS_PROPERTIES = LAYER_PROPERTIES
predict_all: Incomplete

def format_function(
    what: Incomplete,
    name: Incomplete,
    group: Incomplete,
    variant: Incomplete,
    attribute: Incomplete,
    image: Incomplete,
    image_format: Incomplete,
    **kwargs,
) -> Incomplete: ...
def resolve_image(img: Imageable) -> Incomplete: ...
def resolve_at(at: RawBlock | Transform | Iterable[Transform]) -> tuple[Transform, ...]: ...

class When(python_object):
    def __init__(self) -> None: ...
    def check(self, attributes: set[str]) -> bool: ...
    @staticmethod
    def parse(l: Incomplete) -> When: ...

class WhenOr(When):
    left: Incomplete
    right: Incomplete
    def __init__(self, left: Incomplete, right: Incomplete, /) -> None: ...
    def check(self, attributes: Incomplete) -> Incomplete: ...
    @staticmethod
    def parse(l: Incomplete) -> When: ...

class WhenAnd(When):
    left: Incomplete
    right: Incomplete
    def __init__(self, left: Incomplete, right: Incomplete, /) -> None: ...
    def check(self, attributes: Incomplete) -> Incomplete: ...
    @staticmethod
    def parse(l: Incomplete) -> When: ...

class WhenNot(When):
    when: Incomplete
    def __init__(self, when: Incomplete, /) -> None: ...
    def check(self, attributes: Incomplete) -> Incomplete: ...
    @staticmethod
    def parse(l: Incomplete) -> When: ...

class WhenAttribute(When):
    attribute: Incomplete
    def __init__(self, attribute: Incomplete, /) -> None: ...
    def check(self, attributes: Incomplete) -> Incomplete: ...
    @staticmethod
    def parse(l: Incomplete) -> When: ...

class Layer:
    group_args: Incomplete
    at: Incomplete
    when: Incomplete
    if_all: Incomplete
    if_any: Incomplete
    if_not: Incomplete
    transform_args: Incomplete
    def __init__(
        self,
        if_all: Incomplete = [],
        if_any: Incomplete = [],
        if_not: Incomplete = [],
        at: Incomplete = (),
        group_args: Incomplete = {},
        *,
        when: When | str | None = None,
        **kwargs: Incomplete,
    ) -> None: ...
    def check(self, attributes: Incomplete) -> Incomplete: ...
    def wrap(self, d: Incomplete) -> Incomplete: ...
    def apply_format(self, li: LayeredImage, /) -> Incomplete: ...
    def get_displayable(self, attributes: Incomplete) -> None: ...

class Attribute(Layer):
    group: Incomplete
    raw_attribute: Incomplete
    attribute: Incomplete
    image: Incomplete
    default: Incomplete
    variant: Incomplete
    def __init__(
        self,
        group: Incomplete,
        attribute: Incomplete,
        image: Incomplete = None,
        default: bool = False,
        *,
        prefix: Incomplete = None,
        variant: Incomplete = None,
        **kwargs: Incomplete,
    ) -> None: ...
    def apply_format(self, li: LayeredImage) -> Incomplete: ...
    def get_displayable(self, attributes: Incomplete) -> Incomplete: ...

class Condition(Layer):
    at: Incomplete
    condition: Incomplete
    image: Incomplete
    def __init__(self, condition: Incomplete, image: Incomplete, **kwargs: Incomplete) -> None: ...
    def apply_format(self, li: LayeredImage) -> Incomplete: ...
    def get_displayable(self, attributes: Incomplete) -> Incomplete: ...

class ConditionGroup(Layer):
    conditions: Incomplete
    def __init__(self, conditions: Incomplete) -> None: ...
    def apply_format(self, li: LayeredImage) -> Incomplete: ...
    def get_displayable(self, attributes: Incomplete) -> Incomplete: ...

class Always(Layer):
    image: Incomplete
    def __init__(self, image: Incomplete, **kwargs) -> None: ...
    def apply_format(self, li: LayeredImage) -> Incomplete: ...
    def get_displayable(self, attributes: Incomplete) -> Incomplete: ...

class LayeredImage:
    attribute_function: Incomplete
    transform_args: Incomplete
    offer_screen: Incomplete
    name: Incomplete
    image_format: Incomplete
    format_function: Incomplete
    attributes: list[Attribute]
    layers: list[Layer]
    attribute_to_groups: defaultdict[str, set[str]]
    group_to_attributes: defaultdict[str, set[str]]
    at: Incomplete
    fixed_args: Incomplete
    def __init__(
        self,
        attributes: Incomplete,
        at: Incomplete = [],
        name: Incomplete = None,
        image_format: Incomplete = None,
        format_function: Incomplete = ...,
        attribute_function: Incomplete = None,
        offer_screen: Incomplete = None,
        **kwargs,
    ) -> None: ...
    def format(
        self,
        what: Incomplete,
        attribute: Incomplete = None,
        group: Incomplete = None,
        variant: Incomplete = None,
        image: Incomplete = None,
    ) -> Incomplete: ...
    def add(self, a: Incomplete) -> None: ...
    def get_banned(self, attributes: Incomplete) -> Incomplete: ...

def parse_property(
    l: Incomplete, final_properties: dict, expr_properties: dict, names: Container[str]
) -> Literal[0] | Literal[1] | Literal[2]: ...
def parse_displayable(l: Incomplete) -> Imageable: ...

class RawAttribute(renpy.object.Object):
    __version__: int
    expr_properties: Incomplete
    final_properties: Incomplete
    def after_upgrade(self, version: int) -> Incomplete: ...
    name: Incomplete
    image: Imageable
    def __init__(self, name: Incomplete) -> None: ...
    def execute(self, group_name: Incomplete = None, **group_properties) -> Incomplete: ...

def parse_attribute(l: Incomplete) -> Incomplete: ...

class RawAttributeGroup(renpy.object.Object):
    __version__: int
    expr_properties: Incomplete
    final_properties: Incomplete
    group_name: Incomplete
    li_name: Incomplete
    def after_upgrade(self, version: int) -> Incomplete: ...
    children: Incomplete
    def __init__(self, li_name: Incomplete, group_name: str | None) -> None: ...
    def execute(self) -> Incomplete: ...

def parse_group(l: Incomplete, li_name: Incomplete) -> Incomplete: ...

class RawCondition(renpy.object.Object):
    __version__: int
    expr_properties: Incomplete
    final_properties: Incomplete
    def after_upgrade(self, version: int) -> Incomplete: ...
    condition: Incomplete
    image: Imageable
    def __init__(self, condition: Incomplete) -> None: ...
    def execute(self) -> Incomplete: ...

def parse_condition(l: Incomplete, need_expr: Incomplete) -> Incomplete: ...

class RawConditionGroup:
    conditions: Incomplete
    def __init__(self, conditions: list | tuple = ()) -> None: ...
    def execute(self) -> Incomplete: ...

def parse_conditions(l: Incomplete) -> Incomplete: ...

class RawAlways(renpy.object.Object):
    __version__: int
    expr_properties: Incomplete
    final_properties: Incomplete
    def after_upgrade(self, version: int) -> Incomplete: ...
    image: Imageable
    def __init__(self) -> None: ...
    def execute(self) -> Incomplete: ...

def parse_always(l: Incomplete) -> Incomplete: ...

class RawLayeredImage(renpy.object.Object):
    __version__: int
    expr_properties: Incomplete
    final_properties: Incomplete
    def after_upgrade(self, version: int) -> Incomplete: ...
    name: Incomplete
    children: list[RawAlways | RawAttribute | RawAttributeGroup | RawConditionGroup]
    def __init__(self, name: Incomplete) -> None: ...
    def execute(self) -> None: ...

def execute_layeredimage(rai: Incomplete) -> None: ...
def parse_layeredimage(l: Incomplete) -> Incomplete: ...
def lint_layeredimage(rli: RawLayeredImage) -> None: ...

class LayeredImageProxy:
    name: Incomplete
    transform: Incomplete
    def __init__(self, name: Incomplete, transform: Incomplete = None) -> None: ...
    @property
    def image(self) -> Incomplete: ...
    def filter_attributes(self, attributes: Incomplete) -> Incomplete: ...
