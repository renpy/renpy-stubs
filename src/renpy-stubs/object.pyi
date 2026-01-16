from typing import Callable

class Object:
    __version__: int
    nosave: list[str]
    after_setstate: Callable[[], None] | None

sentinels: dict[str, Sentinel]

class Sentinel:
    name: str
    def __new__(cls, name: str) -> Sentinel: ...
    def __init__(self, name: str) -> None: ...
