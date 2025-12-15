import renpy
from _typeshed import Incomplete as Incomplete
from renpy.display.core import Interface as Interface
from renpy.execution import Context as Context
from renpy.rollback import RollbackLog as RollbackLog
from renpy.script import Script as Script
from types import TracebackType
from typing import Any

basepath: Incomplete
searchpath: Incomplete
args: Any
script: Script | None
contexts: Incomplete
interface: Interface | None
lint: bool
log: RollbackLog | None
exception_info: str
style: Incomplete
seen_session: dict[Any, bool]
seen_translates_count: int
new_translates_count: int
after_rollback: bool
post_init: Incomplete
less_memory: bool
less_updates: bool
less_mouse: bool
less_imagedissolve: bool
persistent: Any
preferences: Any
initcode_ast_id: int
build_info: dict[str, Any]

class ExceptionInfo:
    s: Incomplete
    args: Incomplete
    def __init__(self, s, args=()) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(
        self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None
    ): ...

class RestartContext(Exception): ...
class RestartTopContext(Exception): ...

class FullRestartException(Exception):
    reason: Incomplete
    def __init__(self, reason: str = "end_game") -> None: ...

class UtterRestartException(Exception): ...

class QuitException(Exception):
    relaunch: Incomplete
    status: Incomplete
    def __init__(self, relaunch: bool = False, status: int = 0) -> None: ...

class JumpException(Exception): ...
class JumpOutException(Exception): ...

class CallException(Exception):
    from_current: bool
    label: Incomplete
    args: Incomplete
    kwargs: Incomplete
    def __init__(self, label, args, kwargs, from_current: bool = False) -> None: ...
    def __reduce__(self): ...

class EndReplay(Exception): ...
class ParseErrorException(Exception): ...

CONTROL_EXCEPTIONS: Incomplete

def context(index: int = -1) -> renpy.execution.Context: ...
def invoke_in_new_context(callable, *args, **kwargs): ...
def call_in_new_context(label, *args, **kwargs): ...
def call_replay(label, scope={}) -> None: ...
