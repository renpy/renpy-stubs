from _typeshed import Incomplete as Incomplete

def combine_redraw(a: Incomplete, b: Incomplete) -> Incomplete: ...
def to_uniform_value(
    shader_name: Incomplete, uniform_name: Incomplete, variable_types: Incomplete, value: Incomplete
) -> Incomplete: ...

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
        shader: Incomplete,
        uniforms: Incomplete,
        variable_types: Incomplete = None,
        extra_slow_time: float = 0.0,
        extra_slow_duration: float = 0.0,
        redraw: Incomplete = None,
        redraw_when_slow: float = 0.0,
        include_default: bool = True,
        adjust_function: Incomplete = None,
        adjust_name_map: Incomplete = None,
        doc: Incomplete = None,
    ) -> None: ...
    def __hash__(self) -> int: ...
    def __eq__(self, other: object) -> bool: ...
    def combine(self, other: Incomplete) -> Incomplete: ...
    def copy(self, new_uniforms: Incomplete) -> Incomplete: ...

def compute_times(shaders: Incomplete) -> Incomplete: ...
def create_textshader_args_dict(name: Incomplete, shader: Incomplete, s: Incomplete) -> Incomplete: ...
def parse_textshader(o: Incomplete) -> Incomplete: ...

parsed_shader_cache: Incomplete

def get_textshader(o: Incomplete) -> Incomplete: ...
def register_textshader(
    name: Incomplete,
    shaders: Incomplete = ...,
    extra_slow_time: float = 0.0,
    extra_slow_duration: float = 0.0,
    redraw: Incomplete = None,
    redraw_when_slow: float = 0.0,
    include_default: bool = True,
    adjust_function: Incomplete = None,
    doc: Incomplete = None,
    **kwargs,
) -> None: ...
