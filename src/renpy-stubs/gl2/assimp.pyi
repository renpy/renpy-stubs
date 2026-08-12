from _frozen_importlib import BuiltinImporter as BuiltinImporter
from _typeshed import Incomplete

import threading
from typing import Any, Iterable

import renpy
from renpy.gl2.gl2mesh3 import Mesh3

Data = renpy.display.im.Data
Displayable = renpy.display.displayable.Displayable
GL2Model = renpy.gl2.gl2model.GL2Model
Render = renpy.display.render.Render
Matrix = renpy.display.matrix.Matrix
type UniformValue = float | tuple[float, float] | tuple[float, float, float] | tuple[float, float, float, float]

TEXTURE_TYPES: dict[str, int]

class MeshInfo:
    mesh: Mesh3
    shaders: Iterable[str]
    uniforms: dict[str, UniformValue]
    texture_uniforms: dict[str, Displayable]
    twosided: bool
    def __init__(
        self,
        loader: Loader,
        mesh: Mesh3,
        material_index: int,
        textures: Iterable[str],
        shaders: Iterable[str],
    ) -> None: ...

class BlitInfo:
    reverse: Matrix
    forward: Matrix
    mesh_info: MeshInfo
    def __init__(self, reverse: Matrix, forward: Matrix, mesh_info: MeshInfo) -> None: ...

class GLTFModel(renpy.display.displayable.Displayable):
    filename: str
    shaders: Iterable[str]
    tangents: bool
    zoom: float
    uniforms: dict[str, object]
    texture_uniforms: dict[str, Displayable]
    report: bool
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
    def load(self) -> ModelData: ...
    def predict_one(self) -> None: ...
    def render(self, width: float, height: float, st: float, at: float) -> Render: ...
    def visit(self) -> list[Displayable]: ...

class Loader:
    dirname: str
    model_data: ModelData
    mesh_info: dict[int, MeshInfo]
    tangents: bool
    shaders: Iterable[str | Displayable]
    uniforms: set[Incomplete]
    textures: dict[tuple[int, int], Displayable | None]
    filename: str
    def get_material_uniforms(self, material_index: int) -> dict[str, UniformValue]: ...
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
    ) -> ModelData: ...
    def load_mesh(self, mesh_index: int) -> MeshInfo: ...
    def load_textures(self) -> None: ...

class ModelData:
    filename: str
    embedded_textures: dict[str, Data]
    blit_info: list[BlitInfo]
    mesh_info: list[MeshInfo]
    def __init__(self) -> None: ...
    def report(self) -> None: ...

cache: dict[GLTFModel, ModelData]
predicted: set[GLTFModel] | None = None
new_predicted: set[GLTFModel] = set()
loader: Loader
loader_lock: threading.Lock

def finish_predict() -> None: ...
def free_memory() -> None: ...
def preload() -> None: ...
