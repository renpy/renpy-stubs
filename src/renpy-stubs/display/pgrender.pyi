import renpy.pygame as pygame
from _typeshed import Incomplete as Incomplete
from renpy.pygame import Surface as Surface

sample_alpha: Incomplete
sample_noalpha: Incomplete

def set_rgba_masks() -> None: ...

class Surface(pygame.Surface):
    def convert_alpha(self, surface=None): ...
    def convert(self, surface=None): ...
    def copy(self): ...
    def subsurface(self, rect): ...

def surface(rect, alpha): ...

surface_unscaled = surface

def copy_surface(surf, alpha: bool = True): ...

copy_surface_unscaled = copy_surface
safe_formats: Incomplete
image_load_lock: Incomplete
formats: Incomplete

def load_image(f, filename, size=None): ...

load_image_unscaled = load_image

def flip(surf, horizontal, vertical): ...

flip_unscaled = flip

def rotozoom(surf, angle, zoom): ...

rotozoom_unscaled = rotozoom

def transform_scale(surf, size): ...

transform_scale_unscaled = transform_scale

def transform_rotate(surf, angle): ...

transform_rotate_unscaled = transform_rotate
