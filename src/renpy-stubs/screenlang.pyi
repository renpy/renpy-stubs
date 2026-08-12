import renpy
from renpy.object import Object as Object

class ScreenLangScreen(renpy.object.Object):
    __version__: int
    variant: str
    predict: str
    parameters: renpy.parameter.Signature | None
    location: tuple[str, int] | None
    name: str
    modal: str
    zorder: str
    tag: str | None
    code: renpy.python.PyCode | None
    def __init__(self) -> None: ...
    def after_upgrade(self, version: int) -> None: ...
    def define(self, location: tuple[str, int]) -> None: ...
    def __call__(self, *args: Any, **kwargs: Any) -> None: ...
