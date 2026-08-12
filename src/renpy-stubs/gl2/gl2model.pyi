from _frozen_importlib import BuiltinImporter as BuiltinImporter
from typing import Any
from renpy.display.matrix import Matrix
from renpy.gl2.gl2mesh import Mesh
from renpy.gl2.gl2texture import Texture

class GL2Model:
    width: int
    height: int
    mesh: Mesh
    forward: Matrix
    reverse: Matrix
    shaders: tuple[str, ...]
    uniforms: dict[str, Any] | None
    properties: dict[str, Any] | None
    cached_texture: Texture | None
    tex0: GL2Model | None
    tex1: GL2Model | None
    tex2: GL2Model | None
    tex3: GL2Model | None
    def __init__(
        self,
        size: tuple[int, int],
        mesh: Mesh,
        shaders: tuple[str, ...],
        uniforms: dict[str, Any] | None = None,
        properties: dict[str, Any] | None = None,
    ) -> None: ...
    def copy(self) -> GL2Model: ...
    def get_size(self) -> tuple[int, int]: ...
    def get_texture(self, i: int) -> GL2Model: ...
    def load(self) -> None: ...
    def scale(self, factor: float) -> GL2Model: ...
    def set_texture(self, i: int, texture: GL2Model) -> None: ...
    def subsurface(self, rect: tuple[float, float, float, float]) -> GL2Model: ...
