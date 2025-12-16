from _typeshed import Incomplete as Incomplete

class Object:
    __version__: int
    nosave: Incomplete
    after_setstate: Incomplete

sentinels: Incomplete

class Sentinel:
    def __new__(cls, name): ...
    name: Incomplete
    def __init__(self, name) -> None: ...
    def __reduce__(self): ...
