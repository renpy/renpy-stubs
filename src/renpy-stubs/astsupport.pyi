from typing import Any

def hash32(s: Any) -> int: ...
def hash64(s: Any) -> int: ...

class PyExpr(str):
    filename: str
    linenumber: int
    py: int
    hashcode: int
    column: int
    def __new__(
        cls, s: str, filename: str, linenumber: int, py: int = 3, hashcode: int | None = None, column: int = 0, /
    ) -> PyExpr: ...
    @staticmethod
    def checkpoint() -> Any: ...
    @staticmethod
    def revert(opaque: Any) -> None: ...

def make_pyexpr(s: str, filename: str, linenumber: int, column: int, text: str, pos: int) -> PyExpr: ...
