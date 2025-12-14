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

class ScreenLangScreen(renpy.object.Object):
    __version__: int
    variant: str
    predict: str
    parameters: Incomplete
    location: Incomplete
    name: str
    modal: str
    zorder: str
    tag: Incomplete
    code: Incomplete
    def __init__(self) -> None: ...
    def after_upgrade(self, version) -> None: ...
    def define(self, location) -> None: ...
    def __call__(self, *args, **kwargs) -> None: ...
