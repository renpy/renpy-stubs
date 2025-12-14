from typing import Any

def hash32(s: Any) -> int:
    """
    Returns a stable 32-bit hash of the string `s`.

    `s`
        A unicode string. Other types will be coerced to unicode before hashing.
    """

def hash64(s: Any) -> int:
    """
    Returns a stable 64-bit hash of the string `s`.

    `s`
        A unicode string. Other types will be coerced to unicode before hashing.
    """

class PyExpr(str):
    """
    Represents a string containing python expression.
    """

    filename: str
    linenumber: int
    py: int
    hashcode: int
    column: int

    def __new__(
        cls, s: str, filename: str, linenumber: int, py: int = 3, hashcode: int | None = None, column: int = 0, /
    ) -> PyExpr: ...
    @staticmethod
    def checkpoint() -> Any:
        """
        Checkpoints the pyexpr list. Returns an opaque object that can be used
        with PyExpr.revert to revert the list.
        """

    @staticmethod
    def revert(opaque: Any):
        """
        Reverts the pyexpr list to the state it was in when checkpoint was called.
        """

def make_pyexpr(s: str, filename: str, linenumber: int, column: int, text: str, pos: int) -> PyExpr:
    """
    Used by lexer to make a pyexpr, rapidly adjusting line number and column.

    `s`
        The string that is the expression.

    `filename`
        The name of the file the expression is in.

    `linenumber`
        The line number the logical line starts at.

    `column`
        The column the logical line starts at.

    `text`
        The text of the line.

    `pos`
        The position in the text where the expression starts.
    """
