import argparse
import renpy
from renpy.display.core import Interface as Interface
from renpy.execution import Context as Context
from renpy.rollback import RollbackLog as RollbackLog
from renpy.script import Script as Script
from renpy.types import Unused as Unused
from types import TracebackType
from typing import Any, Callable

basepath: str | None
searchpath: Unused
args: argparse.Namespace | None
script: Script | None
contexts: list["Context"]
interface: Interface | None
lint: bool
log: RollbackLog | None
exception_info: str
style: renpy.style.StyleManager | None
seen_session: dict[renpy.ast.NodeName, bool]
seen_translates_count: int
new_translates_count: int
after_rollback: bool
post_init: list[Callable[[], None]]
less_memory: bool
less_updates: bool
less_mouse: bool
less_imagedissolve: bool
persistent: renpy.persistent.Persistent | None
preferences: renpy.preferences.Preferences | None
initcode_ast_id: int
build_info: dict[str, Any]

class ExceptionInfo:
    s: str
    args: tuple[Any]
    def __init__(self, s: str, args: tuple[Any] = ()) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(
        self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None
    ) -> bool: ...

class RestartContext(Exception): ...
class RestartTopContext(Exception): ...

class FullRestartException(Exception):
    reason: str
    def __init__(self, reason: str = "end_game") -> None: ...

class UtterRestartException(Exception): ...

class QuitException(Exception):
    relaunch: bool
    status: int
    def __init__(self, relaunch: bool = False, status: int = 0) -> None: ...

class JumpException(Exception):
    args: tuple[renpy.ast.NodeName]
    def __init__(self, *args: renpy.ast.NodeName) -> None: ...

class JumpOutException(Exception):
    args: tuple[renpy.ast.NodeName]
    def __init__(self, *args: renpy.ast.NodeName) -> None: ...

class CallException(Exception):
    from_current: bool
    label: renpy.ast.NodeName
    args: tuple[Any]
    kwargs: dict[str, Any]
    def __init__(
        self, label: renpy.ast.NodeName, args: tuple[Any], kwargs: dict[str, Any], from_current: bool = False
    ) -> None: ...
    def __reduce__(self) -> str | tuple[Any, ...]: ...

class EndReplay(Exception): ...
class ParseErrorException(Exception): ...

CONTROL_EXCEPTIONS: tuple[type[BaseException], ...]

def context(index: int = -1) -> renpy.execution.Context: ...
def invoke_in_new_context(callable: Callable[..., Any], *args, **kwargs) -> Any: ...
def call_in_new_context(label: renpy.ast.NodeName, *args, **kwargs) -> Any | None: ...
def call_replay(label: renpy.ast.NodeName, scope: dict[str, Any] = {}) -> None: ...
