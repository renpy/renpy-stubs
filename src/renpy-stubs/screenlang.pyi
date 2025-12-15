import renpy
from _typeshed import Incomplete

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
