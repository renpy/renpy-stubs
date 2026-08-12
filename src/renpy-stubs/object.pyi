from collections.abc import Callable
from typing import Self

class Object:
    __version__: int
    nosave: list[str]
    after_setstate: Callable[[Self], None] | None

sentinels: dict[str, Sentinel]

class Sentinel:
    name: str
    def __new__(cls, name: str) -> Sentinel: ...
    def __init__(self, name: str) -> None: ...
