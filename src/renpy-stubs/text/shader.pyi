from _typeshed import Incomplete as Incomplete
from typing import Iterable, overload, Any, Protocol

@overload
def combine_redraw(a: float, b: float | None) -> float: ...
@overload
def combine_redraw(a: None, b: float | None) -> float | None: ...
@overload
def combine_redraw(a: float | None, b: float) -> float: ...
@overload
def combine_redraw(a: float | None, b: None) -> float | None: ...
def combine_redraw(a: float | None, b: float | None) -> float | None: ...
def to_uniform_value(
    shader_name: str, uniform_name: str, variable_types: dict[str, str], value: Incomplete
) -> Incomplete: ...

class TextShaderAdjustFunction(Protocol):
    def __call__(self, shader: "TextShader", **kwargs: Any) -> None: ...

class TextShader:
    shader: tuple[str, ...]
    extra_slow_time: float
    extra_slow_duration: float
    redraw: float | None
    redraw_when_slow: float
    include_default: bool
    doc: str | None
    uniforms: tuple[tuple[str, Any], ...]
    adjust_function: TextShaderAdjustFunction | None
    adjust_name_map: dict[str, str] | None
    variable_types: dict[str, str] | None
    key: tuple[tuple[str, ...], float, float, float | None, float, bool, tuple[tuple[str, Any], ...]]
    def __init__(
        self,
        shader: str | Iterable[str],
        uniforms: tuple[tuple[str, Any], ...],
        variable_types: dict[str, str] | None = None,
        extra_slow_time: float = 0.0,
        extra_slow_duration: float = 0.0,
        redraw: float | None = None,
        redraw_when_slow: float = 0.0,
        include_default: bool = True,
        adjust_function: TextShaderAdjustFunction | None = None,
        adjust_name_map: dict[str, str] | None = None,
        doc: str | None = None,
    ) -> None: ...
    def __hash__(self) -> int: ...
    def __eq__(self, other: object) -> bool: ...
    def combine(self, other: TextShader) -> TextShader: ...
    def copy(self, new_uniforms: dict[str, Any]) -> TextShader: ...

def compute_times(shaders: Iterable[TextShader]) -> tuple[float, float, float | None, float | None]: ...
def create_textshader_args_dict(name: str, shader: TextShader, s: str) -> Incomplete: ...
@overload
def parse_textshader(o: str | TextShader) -> TextShader: ...
@overload
def parse_textshader(o: None) -> None: ...

parsed_shader_cache: dict[str | None, TextShader | None]

def get_textshader(o: str | None) -> TextShader | None: ...
def register_textshader(
    name: str,
    shaders: str | Iterable[str] = ...,
    extra_slow_time: float = 0.0,
    extra_slow_duration: float = 0.0,
    redraw: float | None = None,
    redraw_when_slow: float = 0.0,
    include_default: bool = True,
    adjust_function: TextShaderAdjustFunction | None = None,
    doc: str | None = None,
    **kwargs,
) -> None: ...
