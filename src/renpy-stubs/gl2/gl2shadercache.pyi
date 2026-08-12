import re
from typing import Iterable
from _typeshed import Incomplete as Incomplete

import renpy
from renpy.gl2.gl2shader import Variable as Variable

type PartTuple = tuple[int | str, str, str]
shader_part: "dict[str, ShaderPart]"

def register_shader(name: str, **kwargs) -> ShaderPart: ...

class ShaderPart:
    name: str
    vertex_functions: str
    fragment_functions: str
    vertex_parts: list[PartTuple]
    fragment_parts: list[PartTuple]
    vertex_variables: set[Variable]
    fragment_variables: set[Variable]
    variable_types: dict[str, str]
    uniforms: list[str]
    raw_variables: str
    def __init__(
        self,
        name: str,
        variables: str = "",
        vertex_functions: str = "",
        fragment_functions: str = "",
        private_uniforms: bool = False,
        **kwargs,
    ) -> None: ...
    def expand_name(self, s: str) -> str: ...
    def expand_match(self, m: re.Match[str]) -> str: ...
    def expand_operation(self, m: re.Match[str]) -> str: ...
    def substitute_name(self, s: str) -> str: ...

cache: Incomplete

def source(
    variables: Iterable[Variable], parts: list[PartTuple], functions: list[str], fragment: bool, gles: bool
) -> str: ...

shader_part_filter_cache: dict[tuple[str, ...], tuple[str, ...]]

class ShaderCache:
    filename: str
    gles: bool
    cache: dict[tuple[str, ...], renpy.gl2.gl2shader.Program]
    missing: set[tuple[str, ...]]
    dirty: bool
    def __init__(self, filename: str, gles: bool) -> None: ...
    def get(self, partnames: tuple[str, ...]) -> renpy.gl2.gl2shader.Program: ...
    def check(self, partnames: tuple[str, ...]) -> bool: ...
    def save(self) -> None: ...
    def load(self) -> None: ...
    def clear(self) -> None: ...
    def log_shader(self, kind: str, partnames: tuple[str, ...], text: str) -> None: ...
