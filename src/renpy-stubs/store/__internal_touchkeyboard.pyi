from _typeshed import Incomplete
from renpy.ui import Action
from renpy.store import DictEquality

class _TouchKeyboardTextInput(Action, DictEquality):
    char: str
    def __init__(self, char: str) -> None: ...
    def __call__(self) -> None: ...

class _TouchKeyboardBackspace(Action, DictEquality):
    def __call__(self) -> None: ...

class _TouchKeyboardReturn(Action, DictEquality):
    def __call__(self) -> None: ...
