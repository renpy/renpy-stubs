from _typeshed import Incomplete
from typing import Literal

from renpy.store.achievement import Backend

steam_maximum_framerate: int
steam_position: Literal["top left", "top right", "bottom left", "bottom right"] | None

class SteamBackend(Backend):
    names: dict[str, str]
    stats: dict[str, tuple[Incomplete | None, int, int]]
    def __init__(self) -> None: ...
    def register(
        self,
        name: str,
        steam: str | None = None,
        steam_stat: Incomplete = None,
        stat_max: int | None = None,
        stat_modulo: int = 1,
        **kwargs: Incomplete,
    ) -> None: ...
    def grant(self, name: str) -> None: ...
    def clear(self, name: str) -> None: ...
    def clear_all(self) -> None: ...
    def progress(self, name: str, completed: int | None) -> None: ...
    def has(self, name: str) -> bool: ...

def steam_preinit() -> None: ...

steam: Incomplete
steamapi: Incomplete
has_steam: bool

def steam_init() -> None: ...
