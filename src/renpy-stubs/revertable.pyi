import random
from _typeshed import Incomplete as Incomplete

FUTURE_FLAGS: Incomplete
mutate_flag: bool

def mutator(method: Incomplete) -> Incomplete: ...

class CompressedList:
    pre: Incomplete
    start: int
    end: int
    post: Incomplete
    def __init__(self, old: Incomplete, new: Incomplete) -> None: ...
    def decompress(self, new: Incomplete) -> Incomplete: ...

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
    def wrapper(method: Incomplete) -> Incomplete: ...
    __add__: Incomplete
    __mul__: Incomplete
    __rmul__: Incomplete
    def __getitem__(self, index: Incomplete) -> Incomplete: ...
    def copy(self) -> Incomplete: ...
    def clear(self) -> None: ...

def revertable_range(*args) -> Incomplete: ...
def revertable_sorted(*args, **kwargs) -> Incomplete: ...

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
    def has_key(self, key: Incomplete) -> Incomplete: ...
    def __or__(self, other: Incomplete) -> Incomplete: ...
    def __ror__(self, other: Incomplete) -> Incomplete: ...
    def __ior__(self, other: Incomplete) -> Incomplete: ...
    def copy(self) -> Incomplete: ...

class RevertableDefaultDict(RevertableDict):
    default_factory: Incomplete
    def __init__(self, default_factory: Incomplete = None, *args, **kwargs) -> None: ...
    def __missing__(self, key: Incomplete) -> Incomplete: ...

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
    def wrapper(method: Incomplete) -> Incomplete: ...
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
    def __new__(cls, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *args, **kwargs) -> None: ...
    def __init_subclass__(cls) -> None: ...
    __setattr__: Incomplete
    __delattr__: Incomplete

class MultiRevertable: ...

def checkpointing(method: Incomplete) -> Incomplete: ...
def list_wrapper(method: Incomplete) -> Incomplete: ...

class RollbackRandom(random.Random):
    def __init__(self) -> None: ...
    setstate: Incomplete
    choices: Incomplete
    sample: Incomplete
    getrandbits: Incomplete
    seed: Incomplete
    random: Incomplete
    def Random(self, seed: Incomplete = None) -> Incomplete: ...

class DetRandom(random.Random):
    stack: Incomplete
    def __init__(self) -> None: ...
    choices: Incomplete
    sample: Incomplete
    def random(self) -> Incomplete: ...
    def pushback(self, l: Incomplete) -> None: ...
    def reset(self) -> None: ...
    def Random(self, seed: Incomplete = None) -> Incomplete: ...
