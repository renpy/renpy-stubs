import renpy
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
from renpy.display.render import render as render

cached: Incomplete

class ImageMapCrop(renpy.display.displayable.Displayable):
    child: Incomplete
    rect: Incomplete
    def __init__(self, child, rect) -> None: ...
    def visit(self): ...
    def render(self, width, height, st, at): ...

class ImageCacheCrop(renpy.display.displayable.Displayable):
    def __init__(self, cache, index) -> None: ...
    def render(self, width, height, st, at): ...

class ImageMapCache(renpy.object.Object):
    enable: Incomplete
    def __init__(self, enable) -> None: ...
    def crop(self, d, rect): ...
    def finish(self) -> None: ...
