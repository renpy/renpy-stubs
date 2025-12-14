import renpy.ui as ui
from renpy.atl import position as position
from renpy.compat import (
    PY2 as PY2,
    basestring as basestring,
    bchr as bchr,
    bord as bord,
    open as open,
    str as str,
    tobytes as tobytes,
    unicode as unicode,
)
from renpy.display.core import absolute as absolute
from renpy.python import store_eval as eval
from renpy.revertable import (
    RevertableDefaultDict as __renpy_defaultdict__,
    RevertableDict as __renpy__dict__,
    RevertableList as __renpy__list__,
    RevertableObject as object,
    RevertableSet as __renpy__set__,
    revertable_range as range,
    revertable_sorted as sorted,
)
from renpy.translation import translate_string as __

__all__ = [
    "PY2",
    "Set",
    "_",
    "__",
    "__renpy__dict__",
    "__renpy__list__",
    "__renpy__set__",
    "_dict",
    "_list",
    "_object",
    "_p",
    "_print",
    "_set",
    "_type",
    "absolute",
    "basestring",
    "bchr",
    "bord",
    "dict",
    "eval",
    "input",
    "list",
    "object",
    "open",
    "position",
    "print",
    "python_dict",
    "python_list",
    "python_object",
    "python_set",
    "range",
    "raw_input",
    "set",
    "sorted",
    "str",
    "tobytes",
    "ui",
    "unicode",
]

xrange = range
unicode = str
python_list = list
_list = list
python_dict = dict
_dict = dict
python_object = object
_object = object
python_set = set
_set = set
_type = type
list = __renpy__list__
dict = __renpy__dict__
defaultdict = __renpy_defaultdict__
set = __renpy__set__
Set = __renpy__set__
_print = print

def print(*args, **kwargs) -> None: ...
def _(s): ...
def _p(s): ...
def input(*args, **kwargs) -> None: ...

raw_input = input
