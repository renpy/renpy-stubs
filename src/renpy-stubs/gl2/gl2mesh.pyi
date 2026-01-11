from _frozen_importlib import BuiltinImporter as BuiltinImporter
from typing import Sequence

class AttributeLayout:
    offset: dict[str, int]
    stride: int
    def add_attribute(self, name: str, length: int) -> None: ...

class Mesh:
    allocated_points: int
    attribute: list[float]
    points: int
    point_size: int
    point_data: list[float]
    layout: AttributeLayout
    allocated_triangles: int
    triangles: list[int]
    def get_triangles(self) -> list[tuple[int, int, int]]: ...
    def set_attribute_data(self, attributes: Sequence[float]) -> None: ...
    def set_geometry_data(self, geometry: Sequence[float]) -> None: ...
    def set_triangle_data(self, triangles: Sequence[int]) -> None: ...

SOLID_LAYOUT: AttributeLayout
TEXTURE_LAYOUT: AttributeLayout
MODEL_N_LAYOUT: AttributeLayout
MODEL_NT_LAYOUT: AttributeLayout
TEXT_LAYOUT: AttributeLayout
