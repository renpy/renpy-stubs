from _frozen_importlib import BuiltinImporter as BuiltinImporter
from _typeshed import Incomplete
from renpy.gl2.gl2draw import GL2DrawingContext
from renpy.gl2.gl2mesh import Mesh
from renpy.gl2.gl2model import GL2Model
from renpy.uguu import GLuint

GLSL_PRECISIONS: set[str]
ATTRIBUTE_TYPES: dict[str, int]
UNIFORM_TYPES: set[str]
VARYING_TYPES: set[str]

class Attribute:
    def __init__(self, name: str | None, location: int, size: int) -> None: ...

class Program:
    name: tuple[str, ...]
    program: GLuint
    vertex: Incomplete
    fragment: Incomplete
    attributes: list[Attribute]
    uniform_setters: list[Incomplete]
    def __init__(self, name: Incomplete, vertex: Incomplete, fragment: Incomplete) -> None: ...
    def draw(self, context: GL2DrawingContext, model: GL2Model, mesh: Mesh) -> None: ...
    def draw_ftl(self, texture: int, mesh: Mesh) -> None: ...
    def find_variables(self, source: str, seen_uniforms: set, samplers: int) -> Incomplete: ...
    def load(self) -> None: ...

class ShaderError(Exception): ...

class Variable:
    storage: str | None
    type: str | None
    name: str
    array: int | None
    line: str
    def __init__(self, shader_name: str, line: str) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
