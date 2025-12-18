from renpy.types import Unused as Unused
from renpy.pygame.surface import Surface as PygameSurface
from io import IOBase
import threading

sample_alpha: PygameSurface | None
sample_noalpha: PygameSurface | None

def set_rgba_masks() -> None: ...

class Surface(PygameSurface):
    def convert_alpha(self, surface: Unused = None) -> PygameSurface: ...
    def convert(self, surface: Unused = None) -> PygameSurface: ...
    def copy(self) -> PygameSurface: ...
    def subsurface(self, rect: tuple[int, int, int, int]) -> PygameSurface: ...

def surface(rect: tuple[int, int], alpha: bool | PygameSurface) -> PygameSurface: ...

surface_unscaled = surface

def copy_surface(surf: PygameSurface, alpha: bool | PygameSurface = True) -> PygameSurface: ...

copy_surface_unscaled = copy_surface
safe_formats: set[str]
image_load_lock: threading.RLock
formats: dict[str, int]

def load_image(f: str | IOBase, filename: str, size: tuple[int, int] | None = None) -> PygameSurface: ...

load_image_unscaled = load_image

def flip(surf: PygameSurface, horizontal: bool, vertical: bool) -> PygameSurface: ...

flip_unscaled = flip

def rotozoom(surf: PygameSurface, angle: float, zoom: float) -> PygameSurface: ...

rotozoom_unscaled = rotozoom

def transform_scale(surf: PygameSurface, size: tuple[int, int]) -> PygameSurface: ...

transform_scale_unscaled = transform_scale

def transform_rotate(surf: PygameSurface, angle: float) -> PygameSurface: ...

transform_rotate_unscaled = transform_rotate
