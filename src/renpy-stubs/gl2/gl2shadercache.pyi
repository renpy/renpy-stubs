from _typeshed import Incomplete

shader_part: Incomplete

def register_shader(name, **kwargs): ...

class ShaderPart:
    name: Incomplete
    vertex_functions: Incomplete
    fragment_functions: Incomplete
    vertex_parts: Incomplete
    fragment_parts: Incomplete
    vertex_variables: Incomplete
    fragment_variables: Incomplete
    variable_types: Incomplete
    uniforms: Incomplete
    raw_variables: Incomplete
    def __init__(
        self,
        name,
        variables: str = "",
        vertex_functions: str = "",
        fragment_functions: str = "",
        private_uniforms: bool = False,
        **kwargs,
    ) -> None: ...
    def expand_name(self, s): ...
    def expand_match(self, m): ...
    def expand_operation(self, m): ...
    def substitute_name(self, s): ...

cache: Incomplete

def source(variables, parts, functions, fragment, gles): ...

shader_part_filter_cache: Incomplete

class ShaderCache:
    filename: Incomplete
    gles: Incomplete
    cache: Incomplete
    missing: Incomplete
    dirty: bool
    def __init__(self, filename, gles) -> None: ...
    def get(self, partnames): ...
    def check(self, partnames): ...
    def save(self) -> None: ...
    def load(self) -> None: ...
    def clear(self) -> None: ...
    def log_shader(self, kind, partnames, text) -> None: ...
