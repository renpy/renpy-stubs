import renpy
from _frozen_importlib import BuiltinImporter as BuiltinImporter
from renpy.gl2.gl2mesh import Mesh as Mesh
from renpy.gl2.gl2mesh import AttributeLayout

class Mesh2(renpy.gl2.gl2mesh.Mesh):
    def __init__(self, layout: AttributeLayout, points: int, triangles: int) -> None: ...
    def add_glyph(
        self,
        tw: float,
        th: float,
        cx: float,
        cy: float,
        index: float,
        left: float,
        top: float,
        right: float,
        bottom: float,
        left_time: float,
        right_time: float,
        ascent: float,
        descent: float,
        xoffset: float,
        yoffset: float,
        pseudo_glyph: float,
    ) -> None: ...
    def crop(self, p: Polygon) -> Mesh2: ...
    def get_point0(self) -> tuple[float, float, float, float]: ...
    def get_points(self) -> list[tuple[float, float, float, float]]: ...
    @staticmethod
    def rectangle(pl: float, pb: float, pr: float, pt: float) -> Mesh2: ...
    def remap_texture(
        self,
        old_x: float,
        old_y: float,
        old_w: float,
        old_h: float,
        new_x: float,
        new_y: float,
        new_w: float,
        new_h: float,
    ) -> None: ...
    @staticmethod
    def text_mesh(glyphs: int) -> Mesh2: ...
    @staticmethod
    def texture_grid_mesh(
        width: int, height: int, pl: float, pb: float, pr: float, pt: float, tl: float, tb: float, tr: float, tt: float
    ) -> Mesh2: ...
    @staticmethod
    def texture_rectangle(
        pl: float, pb: float, pr: float, pt: float, tl: float, tb: float, tr: float, tt: float
    ) -> Mesh2: ...
