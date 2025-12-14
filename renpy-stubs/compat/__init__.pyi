import builtins
from _typeshed import Incomplete

__all__ = ["PY2", "open", "basestring", "str", "pystr", "range", "round", "bord", "bchr", "tobytes", "chr", "unicode"]

PY2: bool
python_open = open
open: Incomplete
compat_open = open
basestring: Incomplete
pystr = str
unicode = str
str = builtins.str

def bord(s: bytes) -> int: ...
def bchr(i: int) -> bytes: ...
def tobytes(s): ...

chr = builtins.chr
range = builtins.range
round: Incomplete
