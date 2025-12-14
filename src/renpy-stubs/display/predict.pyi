from _typeshed import Incomplete
from collections.abc import Generator
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

image: Incomplete
predicted: Incomplete
predicting: bool
screens: Incomplete
tlids = list[str | None]

def displayable(d): ...
def screen(_screen_name, *args, **kwargs) -> None: ...
def reset() -> None: ...
def prediction_coroutine(root_widget) -> Generator[Incomplete, None, Incomplete]: ...
