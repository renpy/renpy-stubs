import renpy
import renpy.gl2.live2dmotion
from _typeshed import Incomplete
from renpy.display.core import absolute as absolute
from renpy.gl2.gl2shadercache import register_shader as register_shader
from typing import Any

did_onetime_init: bool
did_web_init: bool
web_is_incompatible: bool

def onetime_init() -> None: ...
def web_init() -> None: ...

did_init: bool

def init() -> None: ...
def reset() -> None: ...
def reset_states() -> None: ...

class Live2DExpression:
    parameters: Incomplete
    fadein: Incomplete
    fadeout: Incomplete
    def __init__(self, parameters, fadein, fadeout) -> None: ...

class Live2DCommon:
    base: Incomplete
    model_json: Incomplete
    model: Incomplete
    textures: Incomplete
    attributes: Incomplete
    motions: dict[str, renpy.gl2.live2dmotion.Motion | renpy.gl2.live2dmotion.NullMotion]
    expressions: Incomplete
    all_expressions: Incomplete
    nonexclusive: dict[str, Live2DExpression]
    seamless: bool | set[str]
    attribute_function: Any
    attribute_filter: Any
    update_function: Any
    def __init__(self, filename, default_fade) -> None: ...
    def apply_aliases(self, aliases) -> None: ...
    def apply_nonexclusive(self, nonexclusive) -> None: ...
    def apply_seamless(self, value) -> None: ...
    def is_seamless(self, motion): ...

common_cache: Incomplete

class Live2DState:
    mark: bool
    cycle_new: bool
    old: Live2D | None
    new: Live2D | None
    old_base_time: float | None
    new_base_time: float | None
    expressions: Incomplete
    old_expressions: Incomplete
    def __init__(self) -> None: ...
    def update_expressions(self, expressions, now) -> None: ...

states: Incomplete
live2d_showing: bool

def update_states() -> None: ...

class Live2D(renpy.display.displayable.Displayable):
    filename: str
    name: tuple[str, str, str, int] | None
    nosave: Incomplete
    common_cache: Incomplete
    used_nonexclusive: Incomplete
    properties: Incomplete
    default_fade: float
    def create_common(self): ...
    @property
    def common(self): ...
    motions: Incomplete
    expression: Incomplete
    zoom: Incomplete
    top: Incomplete
    base: Incomplete
    height: Incomplete
    loop: Incomplete
    fade: Incomplete
    sustain: Incomplete
    def __init__(
        self,
        filename,
        zoom=None,
        top: float = 0.0,
        base: float = 1.0,
        height: float = 1.0,
        loop: bool = False,
        aliases={},
        fade=None,
        motions=None,
        expression=None,
        nonexclusive=None,
        used_nonexclusive=None,
        seamless=None,
        sustain: bool = False,
        attribute_function=None,
        attribute_filter=None,
        update_function=None,
        default_fade: float = 1.0,
        **properties,
    ) -> None: ...
    unique_time: Incomplete
    unique_serial: int
    def ensure_name(self) -> None: ...
    def per_interact(self) -> None: ...
    def update(self, common, st, st_fade): ...
    def update_expressions(self, st): ...
    def blend_parameter(self, name, blend, value, weight: float = 1.0) -> None: ...
    def blend_opacity(self, name, blend, value, weight: float = 1.0) -> None: ...
    def render(self, width, height, st, at): ...
    def visit(self): ...

def has_live2d(): ...
