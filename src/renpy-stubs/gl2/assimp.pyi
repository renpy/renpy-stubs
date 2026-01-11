import renpy as renpy
from _frozen_importlib import BuiltinImporter as BuiltinImporter
from _typeshed import Incomplete

class BlitInfo:
    def __init__(self, reverse: Matrix, forward: Matrix, mesh_info: MeshInfo) -> None: ...

Data = renpy.display.im.Data
Displayable = renpy.display.displayable.Displayable
GL2Model = renpy.gl2.gl2model.GL2Model

class GLTFModel(renpy.display.displayable.Displayable):
    def __init__(
        self,
        filename: str,
        shader: str | tuple[str] = (),
        tangents: bool = False,
        zoom: float = 1.0,
        report: bool = False,
        **kwargs,
    ) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def load(self) -> None: ...
    def predict_one(self) -> None: ...
    def render(self, width, height, st, at) -> None: ...
    def visit(self) -> None: ...
    filename: str
    shaders: Iterable[str]
    tangents: bool
    zoom: float
    uniforms: dict[str, object]
    texture_uniforms: dict[str, Displayable]
    report: bool

def Iterable(*args, **kwargs) -> None: ...
def Literal(*args, **kwds) -> None: ...

class Loader:
    dirname: str
    model_data: Incomplete
    mesh_info: dict[Incomplete, Incomplete]
    tangents: bool
    shaders: Incomplete
    uniforms: set[Incomplete]
    textures: dict[Incomplete, Incomplete]
    filename: Incomplete

    def __reduce__(self) -> str | tuple[Any, ...]: ...
    def get_material_uniforms(self, material_index: int) -> Incomplete: ...
    def get_texture(self, material_index: int, texture_type: int) -> Displayable | None: ...
    def get_texture_uniforms(self, material_index: int) -> dict[str, Displayable]: ...
    def get_twosided(self, material_index: int) -> bool: ...
    def load(
        self,
        model_data: ModelData,
        filename: str,
        shaders: Iterable[str | Displayable],
        tangents: bool,
        zoom: float,
        report: bool,
    ) -> None: ...
    def load_mesh(self, mesh_index: int) -> MeshInfo: ...
    def load_textures(self) -> None: ...

Matrix = renpy.display.matrix.Matrix

class MeshInfo:
    def __init__(
        self,
        loader: Incomplete,
        mesh: Incomplete,
        material_index: Incomplete,
        textures: Iterable[str],
        shaders: Iterable[str],
    ) -> None: ...
    mesh: Mesh3
    shaders: Iterable[str]
    uniforms: dict[str, object]
    texture_uniforms: dict[str, Displayable]
    twosided: bool

class ModelData:
    def __init__(self) -> None: ...
    def report(self) -> None: ...
    filename: str
    embedded_textures: dict[str, Data]
    blit_info: list[BlitInfo]
    mesh_info: list[MeshInfo]

Render = renpy.display.render.Render

def finish_predict() -> None: ...
def free_memory() -> None: ...
def preload() -> None: ...
def render_for_texture(
    d: Incomplete, width: Incomplete, height: Incomplete, st: Incomplete, at: Incomplete
) -> None: ...
def unoptimized_texture(d: Incomplete) -> None: ...
