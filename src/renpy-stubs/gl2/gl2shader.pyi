from _frozen_importlib import BuiltinImporter as BuiltinImporter
from _typeshed import Incomplete
from renpy.uguu import GLuint

GLSL_PRECISIONS: set[str]
ATTRIBUTE_TYPES: dict[str, int]
UNIFORM_TYPES: set[str]
VARYING_TYPES: set[str]

class Attribute:
    def __init__(self, name: Incomplete, location: int, size: int) -> None: ...

class Program:
    name: Incomplete
    program: GLuint
    vertex: Incomplete
    fragment: Incomplete
    attributes: list[Incomplete]
    uniform_setters: list[Incomplete]

    def __init__(self, name: Incomplete, vertex: Incomplete, fragment: Incomplete) -> None: ...
    def draw(self, context: GL2DrawingContext, model: GL2Model, mesh: Mesh) -> Incomplete: ...
    def draw_ftl(self, texture: int, mesh: Mesh) -> Incomplete: ...
    def find_variables(self, source: Incomplete, seen_uniforms: set, samplers: int) -> Incomplete: ...
    def load(self) -> None: ...

class ShaderError(Exception): ...

class Variable:
    def __init__(self, shader_name: str, line: str) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    storage: str | None
    type: str | None
    name: str | None
    array: int | None
    line: str

def generate_uniform_setter(
    shader_name: str, location: int, uniform_name: str, uniform_type: str, array: int | None, sampler: int
) -> Incomplete: ...
