from _typeshed import Incomplete as Incomplete

class Object:
    __version__: int
    nosave: Incomplete
    after_setstate: Incomplete

sentinels: Incomplete

class Sentinel:
    def __new__(cls, name: Incomplete) -> Incomplete: ...
    name: Incomplete
    def __init__(self, name: Incomplete) -> None: ...
    def __reduce__(self) -> Incomplete: ...
