import renpy
from renpy.display.core import absolute as absolute
from renpy.display.displayable import Displayable as Displayable, DisplayableArguments
from renpy.gl2.gl2shadercache import register_shader as register_shader
from renpy.gl2.live2dmodel import Live2DModel as Live2DModel
from typing import Any, Callable, Iterable, Literal, TypedDict

type Live2DName = tuple[str, str, str, int]
type Live2DAttributeFunction = Callable[[tuple[str, ...]], tuple[str, ...]]
type Live2DUpdateFunction = Callable[[Live2D, float], float | None]
did_onetime_init: bool
did_web_init: bool
web_is_incompatible: bool

def onetime_init() -> None: ...
def web_init() -> None: ...

did_init: bool

def init() -> None: ...
def reset() -> None: ...
def reset_states() -> None: ...

class ExpressionParameter(TypedDict):
    Id: str
    Value: float
    Blend: Literal["Add", "Multiply", "Overwrite"]

class Live2DExpression:
    parameters: list[ExpressionParameter]
    fadein: float
    fadeout: float
    def __init__(self, parameters: list[ExpressionParameter], fadein: float, fadeout: float) -> None: ...

class Live2DCommon:
    base: str
    model_json: dict[str, Any]
    model: Live2DModel
    textures: list[Displayable]
    attributes: set[str]
    motions: dict[str, renpy.gl2.live2dmotion.BaseMotion]
    expressions: dict[str, Live2DExpression]
    all_expressions: dict[str, Live2DExpression]
    nonexclusive: dict[str, Live2DExpression]
    seamless: bool | set[str]
    attribute_function: Live2DAttributeFunction | None
    attribute_filter: Live2DAttributeFunction | None
    update_function: Live2DUpdateFunction | None
    def __init__(self, filename: str, default_fade: float) -> None: ...
    def apply_aliases(self, aliases: dict[str, str]) -> None: ...
    def apply_nonexclusive(self, nonexclusive: Iterable[str]) -> None: ...
    def apply_seamless(self, value: bool | set[str]) -> None: ...
    def is_seamless(self, motion: str) -> bool: ...

common_cache: dict[tuple[str, float], Live2DCommon]

class Live2DState:
    mark: bool
    cycle_new: bool
    old: Live2D | None
    new: Live2D | None
    old_base_time: float | None
    new_base_time: float | None
    expressions: list[tuple[str, float]]
    old_expressions: list[tuple[str, float, float]]
    def __init__(self) -> None: ...
    def update_expressions(self, expressions: list[str], now: float) -> None: ...

states: dict[Live2DName, Live2DState]
live2d_showing: bool

def update_states() -> None: ...

class Live2D(renpy.display.displayable.Displayable):
    filename: str
    name: Live2DName | None
    nosave: list[str]
    common_cache: Live2DCommon | None
    _duplicatable: bool
    used_nonexclusive: list[str] | None
    properties: dict[str, Any]
    default_fade: float
    def create_common(self) -> Live2DCommon: ...
    @property
    def common(self) -> Live2DCommon: ...
    motions: list[str] | None
    expression: str | None
    zoom: float | None
    top: float
    base: float
    height: float
    loop: bool
    fade: bool | None
    sustain: bool
    def __init__(
        self,
        filename: str,
        zoom: float | None = None,
        top: float = 0.0,
        base: float = 1.0,
        height: float = 1.0,
        loop: bool = False,
        aliases: dict[str, str] = {},
        fade: bool | None = None,
        motions: list[str] | None = None,
        expression: str | None = None,
        nonexclusive: Iterable[str] | None = None,
        used_nonexclusive: list[str] | None = None,
        seamless: bool | set[str] | None = None,
        sustain: bool = False,
        attribute_function: Live2DAttributeFunction | None = None,
        attribute_filter: Live2DAttributeFunction | None = None,
        update_function: Live2DUpdateFunction | None = None,
        default_fade: float = 1.0,
        **properties,
    ) -> None: ...
    unique_time: str
    unique_serial: int
    def ensure_name(self) -> None: ...
    def per_interact(self) -> None: ...
    def _duplicate(self, args: DisplayableArguments | None) -> Live2D: ...
    def _list_attributes(self, tag: str, attributes: Iterable[str]) -> list[str]: ...
    def _choose_attributes(self, tag: str, attributes: Iterable[str], optional: Iterable[str]) -> tuple[str, ...]: ...
    def update(self, common: Live2DCommon, st: float, st_fade: float | None) -> float | None: ...
    def update_expressions(self, st: float) -> float | None: ...
    def blend_parameter(self, name: str, blend: str, value: float, weight: float = 1.0) -> None: ...
    def blend_opacity(self, name: str, blend: str, value: float, weight: float = 1.0) -> None: ...
    def render(self, width: float, height: float, st: float, at: float) -> renpy.display.render.Render: ...
    def visit(self) -> list[Displayable]: ...

_has_live2d: bool | None

def has_live2d() -> bool: ...
