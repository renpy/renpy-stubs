from collections.abc import Callable

from renpy.display.matrix import Matrix
from renpy.store import DictEquality, _BaseMatrix

class TransformMatrix(_BaseMatrix):
    function: Callable[..., Matrix] | None
    nargs: int
    args: tuple[float, ...]
    def __init__(self, *args: float) -> None: ...
    def __call__(self, other: _BaseMatrix, done: float) -> Matrix: ...
    @staticmethod
    def _document(function: Callable) -> str: ...

class OffsetMatrix(TransformMatrix, DictEquality):
    nargs: int
    function: Callable[[float, float, float], Matrix]
    __doc__: str

class RotateMatrix(TransformMatrix, DictEquality):
    nargs: int
    function: Callable[[float, float, float], Matrix]
    __doc__: str

class ScaleMatrix(TransformMatrix, DictEquality):
    nargs: int
    function: Callable[[float, float, float], Matrix]
    __doc__: str
