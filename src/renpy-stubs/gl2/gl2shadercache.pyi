from _typeshed import Incomplete as Incomplete

shader_part: Incomplete

def register_shader(name: Incomplete, **kwargs) -> Incomplete: ...

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
        name: Incomplete,
        variables: str = "",
        vertex_functions: str = "",
        fragment_functions: str = "",
        private_uniforms: bool = False,
        **kwargs,
    ) -> None: ...
    def expand_name(self, s: Incomplete) -> Incomplete: ...
    def expand_match(self, m: Incomplete) -> Incomplete: ...
    def expand_operation(self, m: Incomplete) -> Incomplete: ...
    def substitute_name(self, s: Incomplete) -> Incomplete: ...

cache: Incomplete

def source(
    variables: Incomplete, parts: Incomplete, functions: Incomplete, fragment: Incomplete, gles: Incomplete
) -> Incomplete: ...

shader_part_filter_cache: Incomplete

class ShaderCache:
    filename: Incomplete
    gles: Incomplete
    cache: Incomplete
    missing: Incomplete
    dirty: bool
    def __init__(self, filename: Incomplete, gles: Incomplete) -> None: ...
    def get(self, partnames: Incomplete) -> Incomplete: ...
    def check(self, partnames: Incomplete) -> Incomplete: ...
    def save(self) -> None: ...
    def load(self) -> None: ...
    def clear(self) -> None: ...
    def log_shader(self, kind: Incomplete, partnames: Incomplete, text: Incomplete) -> None: ...
