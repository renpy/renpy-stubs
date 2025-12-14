from _typeshed import Incomplete
from renpy.compat import (
    PY2 as PY2,
    basestring as basestring,
    bchr as bchr,
    bord as bord,
    chr as chr,
    open as open,
    pystr as pystr,
    range as range,
    round as round,
    str as str,
    tobytes as tobytes,
    unicode as unicode,
)

def real(s): ...
def scale(n): ...
def real_bilinear(src, size): ...
def real_transform_scale(surf, size): ...
def image_load_unscaled(f, hint, convert: bool = True): ...
def image_save_unscaled(surf, filename) -> None: ...
def surface_scale(full): ...

real_renpy_pixellate: Incomplete
real_renpy_transform: Incomplete

def real_smoothscale(src, size, dest=None): ...

smoothscale = real_smoothscale
