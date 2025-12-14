import random
from _typeshed import Incomplete
from renpy.compat import (
    PY2 as PY2,
    basestring as basestring,
    bchr as bchr,
    bord as bord,
    chr as chr,
    open as open,
    pystr as pystr,
    range as range,
    round as round,
    str as str,
    tobytes as tobytes,
    unicode as unicode,
)

FUTURE_FLAGS: Incomplete
mutate_flag: bool

def mutator(method): ...

class CompressedList:
    pre: Incomplete
    start: int
    end: int
    post: Incomplete
    def __init__(self, old, new) -> None: ...
    def decompress(self, new): ...

class RevertableList(list):
    def __init__(self, *args) -> None: ...
    __delitem__: Incomplete
    __setitem__: Incomplete
    __iadd__: Incomplete
    __imul__: Incomplete
    append: Incomplete
    extend: Incomplete
    insert: Incomplete
    pop: Incomplete
    remove: Incomplete
    reverse: Incomplete
    sort: Incomplete
    def wrapper(method): ...
    __add__: Incomplete
    __mul__: Incomplete
    __rmul__: Incomplete
    def __getitem__(self, index): ...
    def copy(self): ...
    def clear(self) -> None: ...

def revertable_range(*args): ...
def revertable_sorted(*args, **kwargs): ...

class RevertableDict(dict):
    def __init__(self, *args, **kwargs) -> None: ...
    __delitem__: Incomplete
    __setitem__: Incomplete
    clear: Incomplete
    pop: Incomplete
    popitem: Incomplete
    setdefault: Incomplete
    update: Incomplete
    itervalues: Incomplete
    iterkeys: Incomplete
    iteritems: Incomplete
    def has_key(self, key): ...
    def __or__(self, other): ...
    def __ror__(self, other): ...
    def __ior__(self, other): ...
    def copy(self): ...

class RevertableDefaultDict(RevertableDict):
    default_factory: Incomplete
    def __init__(self, default_factory=None, *args, **kwargs) -> None: ...
    def __missing__(self, key): ...

class RevertableSet(set):
    __reduce__: Incomplete
    __reduce_ex__: Incomplete
    def __init__(self, *args) -> None: ...
    __iand__: Incomplete
    __ior__: Incomplete
    __isub__: Incomplete
    __ixor__: Incomplete
    add: Incomplete
    clear: Incomplete
    difference_update: Incomplete
    discard: Incomplete
    intersection_update: Incomplete
    pop: Incomplete
    remove: Incomplete
    symmetric_difference_update: Incomplete
    union_update: Incomplete
    update: Incomplete
    def wrapper(method): ...
    __and__: Incomplete
    __sub__: Incomplete
    __xor__: Incomplete
    __or__: Incomplete
    copy: Incomplete
    difference: Incomplete
    intersection: Incomplete
    symmetric_difference: Incomplete
    union: Incomplete

class RevertableObject:
    def __new__(cls, *args, **kwargs): ...
    def __init__(self, *args, **kwargs) -> None: ...
    def __init_subclass__(cls) -> None: ...
    __setattr__: Incomplete
    __delattr__: Incomplete

class MultiRevertable: ...

def checkpointing(method): ...
def list_wrapper(method): ...

class RollbackRandom(random.Random):
    def __init__(self) -> None: ...
    setstate: Incomplete
    choices: Incomplete
    sample: Incomplete
    getrandbits: Incomplete
    seed: Incomplete
    random: Incomplete
    def Random(self, seed=None): ...

class DetRandom(random.Random):
    stack: Incomplete
    def __init__(self) -> None: ...
    choices: Incomplete
    sample: Incomplete
    def random(self): ...
    def pushback(self, l) -> None: ...
    def reset(self) -> None: ...
    def Random(self, seed=None): ...
