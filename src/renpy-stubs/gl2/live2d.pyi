import renpy
from _typeshed import Incomplete as Incomplete
from renpy.display.core import absolute as absolute
from renpy.display.displayable import Displayable as Displayable
from renpy.gl2.gl2shadercache import register_shader as register_shader
from _typeshed import Incomplete

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
    def __init__(self, parameters: Incomplete, fadein: Incomplete, fadeout: Incomplete) -> None: ...

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
    def __init__(self, filename: Incomplete, default_fade: Incomplete) -> None: ...
    def apply_aliases(self, aliases: Incomplete) -> None: ...
    def apply_nonexclusive(self, nonexclusive: Incomplete) -> None: ...
    def apply_seamless(self, value: Incomplete) -> None: ...
    def is_seamless(self, motion: Incomplete) -> Incomplete: ...

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
    def update_expressions(self, expressions: Incomplete, now: Incomplete) -> None: ...

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
    def create_common(self) -> Incomplete: ...
    @property
    def common(self) -> Incomplete: ...
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
        filename: Incomplete,
        zoom: Incomplete = None,
        top: float = 0.0,
        base: float = 1.0,
        height: float = 1.0,
        loop: bool = False,
        aliases: Incomplete = {},
        fade: Incomplete = None,
        motions: Incomplete = None,
        expression: Incomplete = None,
        nonexclusive: Incomplete = None,
        used_nonexclusive: Incomplete = None,
        seamless: Incomplete = None,
        sustain: bool = False,
        attribute_function: Incomplete = None,
        attribute_filter: Incomplete = None,
        update_function: Incomplete = None,
        default_fade: float = 1.0,
        **properties,
    ) -> None: ...
    unique_time: Incomplete
    unique_serial: int
    def ensure_name(self) -> None: ...
    def per_interact(self) -> None: ...
    def update(self, common: Incomplete, st: Incomplete, st_fade: Incomplete) -> Incomplete: ...
    def update_expressions(self, st: Incomplete) -> Incomplete: ...
    def blend_parameter(self, name: Incomplete, blend: Incomplete, value: Incomplete, weight: float = 1.0) -> None: ...
    def blend_opacity(self, name: Incomplete, blend: Incomplete, value: Incomplete, weight: float = 1.0) -> None: ...
    def render(self, width: Incomplete, height: Incomplete, st: Incomplete, at: Incomplete) -> Incomplete: ...
    def visit(self) -> Incomplete: ...

def has_live2d() -> Incomplete: ...
