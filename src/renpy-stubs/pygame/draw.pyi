from _frozen_importlib import BuiltinImporter as BuiltinImporter
from typing import TYPE_CHECKING

import renpy
from renpy.pygame.rect import Rect as Rect
from renpy.pygame.surface import Surface as Surface

if TYPE_CHECKING:
    type ColorLikeNoStr = tuple[int, int, int, int] | tuple[int, int, int] | int | renpy.pygame.color.Color

def aaline(
    surface: Surface, color: ColorLikeNoStr, startpos: tuple[int, int], endpos: tuple[int, int], blend: int = 1
) -> Rect: ...
def aalines(
    surface: Surface, color: ColorLikeNoStr, closed: bool, pointlist: list[tuple[int, int]], blend: int = 1
) -> Rect: ...
def arc(
    surface: Surface,
    color: ColorLikeNoStr,
    rect: Rect | tuple[int, int, int, int],
    start_angle: float,
    stop_angle: float,
    width: int = 1,
) -> Rect: ...
def circle(surface: Surface, color: ColorLikeNoStr, pos: tuple[int, int], radius: int, width: int = 0) -> Rect: ...
def ellipse(
    surface: Surface, color: ColorLikeNoStr, rect: Rect | tuple[int, int, int, int], width: int = 0
) -> Rect: ...
def line(
    surface: Surface, color: ColorLikeNoStr, start_pos: tuple[int, int], end_pos: tuple[int, int], width: int = 1
) -> Rect: ...
def lines(
    surface: Surface, color: ColorLikeNoStr, closed: bool, pointlist: list[tuple[int, int]], width: int = 1
) -> Rect: ...
def polygon(surface: Surface, color: ColorLikeNoStr, pointlist: list[tuple[int, int]], width: int = 0) -> Rect: ...
def rect(surface: Surface, color: ColorLikeNoStr, rect: Rect | tuple[int, int, int, int], width: int = 0) -> Rect: ...
