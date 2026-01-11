from _frozen_importlib import BuiltinImporter as BuiltinImporter
from _typeshed import Incomplete
from renpy.display.matrix import Matrix
from renpy.gl2.gl2mesh import Mesh

class GL2Model:
    width: int
    height: int
    mesh: Mesh
    forward: Matrix
    reverse: Matrix
    shaders: tuple[Incomplete]
    uniforms: dict[Incomplete, Incomplete]
    properties: dict[Incomplete, Incomplete]
    cached_texture: Incomplete

    def __init__(
        self,
        size: tuple[int, int],
        mesh: Incomplete,
        shaders: Incomplete,
        uniforms: Incomplete = None,
        properties: Incomplete = None,
    ) -> None: ...
    def copy(self) -> GL2Model: ...
    def get_size(self) -> tuple[int, int]: ...
    def get_texture(self, i: int) -> GL2Model: ...
    def load(self) -> None: ...
    def scale(self, factor: float) -> GL2Model: ...
    def set_texture(self, i: int, texture: GL2Model) -> None: ...
    def subsurface(self, rect: tuple[float, float, float, float]) -> GL2Model: ...
