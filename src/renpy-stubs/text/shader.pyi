from _typeshed import Incomplete as Incomplete

def combine_redraw(a, b): ...
def to_uniform_value(shader_name, uniform_name, variable_types, value): ...

class TextShader:
    shader: Incomplete
    extra_slow_time: Incomplete
    extra_slow_duration: Incomplete
    redraw: Incomplete
    redraw_when_slow: Incomplete
    include_default: Incomplete
    doc: Incomplete
    uniforms: Incomplete
    adjust_function: Incomplete
    adjust_name_map: Incomplete
    variable_types: Incomplete
    key: Incomplete
    def __init__(
        self,
        shader,
        uniforms,
        variable_types=None,
        extra_slow_time: float = 0.0,
        extra_slow_duration: float = 0.0,
        redraw=None,
        redraw_when_slow: float = 0.0,
        include_default: bool = True,
        adjust_function=None,
        adjust_name_map=None,
        doc=None,
    ) -> None: ...
    def __hash__(self) -> int: ...
    def __eq__(self, other: object) -> bool: ...
    def combine(self, other): ...
    def copy(self, new_uniforms): ...

def compute_times(shaders): ...
def create_textshader_args_dict(name, shader, s): ...
def parse_textshader(o): ...

parsed_shader_cache: Incomplete

def get_textshader(o): ...
def register_textshader(
    name,
    shaders=...,
    extra_slow_time: float = 0.0,
    extra_slow_duration: float = 0.0,
    redraw=None,
    redraw_when_slow: float = 0.0,
    include_default: bool = True,
    adjust_function=None,
    doc=None,
    **kwargs,
) -> None: ...
