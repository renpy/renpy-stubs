from typing import TYPE_CHECKING, Any, Self

import renpy
from renpy.object import Object as Object
from renpy.revertable import RevertableObject as RevertableObject

if TYPE_CHECKING:
    type RollbackIdentifier = tuple[float, int]

class StoreDeleted:
    def __reduce__(self) -> str | tuple[Any, ...]: ...

deleted: StoreDeleted

class SlottedNoRollback: ...
class NoRollback(SlottedNoRollback): ...

class AlwaysRollback(renpy.revertable.RevertableObject):
    def __new__(cls, *args: Any, **kwargs: Any) -> Self: ...

NOROLLBACK_TYPES: tuple[
    type, type, type, type, type
]  # In practice: tuple[type[AlwaysRollback], type[NoRollback], type[SlottedNoRollback], type[StoreDeleted], type[Forward]]

def reached(obj: object, reachable: set[str], wait: object) -> None: ...
def reached_vars(store: str, reachable: set[str], wait: object) -> None: ...

generation: float
serial: int
rng: renpy.revertable.DetRandom

class Forward:
    name: str
    data: Any
    fixed: bool
    def __init__(self, name: str, data: Any, fixed: bool) -> None: ...

class Rollback(renpy.object.Object):
    __version__: int
    identifier: RollbackIdentifier
    not_greedy: bool
    checkpointing_suspended: bool
    fixed: bool
    context: Any
    objects: list[Any]
    purged: bool
    random: list[float]
    forward: Forward | None
    stores: dict[str, Any]
    delta_ebc: Any
    retain_after_load: bool
    checkpoint: bool
    hard_checkpoint: bool
    def __init__(self) -> None: ...
    def after_upgrade(self, version: int) -> None: ...
    def purge_unreachable(self, reachable: set[str], wait: object) -> int: ...
    def rollback(self) -> None: ...
    def rollback_control(self) -> None: ...

class RollbackLog(renpy.object.Object):
    __version__: int
    nosave: set[str]
    identifier_cache: dict[RollbackIdentifier, int]
    force_checkpoint: bool
    log: list[Rollback]
    current: Rollback | None
    mutated: set[str]
    rollback_limit: int
    rollback_block: int
    checkpointing_suspended: bool
    forward: list[Forward]
    old_store: dict[str, dict[str, Any]]
    rolled_forward: bool
    retain_after_load_flag: bool
    did_interaction: bool
    def __init__(self) -> None: ...
    def after_setstate(self) -> None: ...
    ever_been_changed: set[str]
    def after_upgrade(self, version: int) -> None: ...
    def begin(self, force: bool = False) -> None: ...
    def replace_node(self, old: renpy.object.Object, new: renpy.object.Object) -> None: ...
    def complete(self, begin: bool = False) -> None: ...
    def get_roots(self) -> list[Any]: ...
    def purge_unreachable(self, roots: list[Any], wait: object = None) -> None: ...
    def in_rollback(self) -> bool: ...
    def in_fixed_rollback(self) -> bool: ...
    def forward_info(self) -> Any | None: ...
    def checkpoint(self, data: Any | None = None, keep_rollback: bool = False, hard: bool = True) -> None: ...
    def suspend_checkpointing(self, flag: bool) -> None: ...
    def block(self, purge: bool = False) -> None: ...
    def retain_after_load(self) -> None: ...
    def fix_rollback(self) -> None: ...
    def can_rollback(self, checkpoints: int = 1, force: bool = False) -> bool: ...
    def load_failed(self) -> None: ...
    def rollback(
        self,
        checkpoints: int,
        force: bool = False,
        label: str | None = None,
        greedy: bool = True,
        on_load: bool = False,
        abnormal: bool = True,
        current_label: str | None = None,
    ) -> None: ...
    def freeze(self, wait: object = None) -> list[Any]: ...
    def discard_freeze(self) -> None: ...
    def unfreeze(self, roots: list[Any], label: str | None = None) -> None: ...
    def build_identifier_cache(self) -> None: ...
    def get_identifier_checkpoints(self, identifier: RollbackIdentifier) -> int | None: ...

class UnfreezeException(BaseException):
    log: RollbackLog
    roots: dict[str, Any] | None
    label: str | None
    def __init__(self, log: RollbackLog, roots: dict[str, Any] | None = None, label: str | None = None) -> None: ...
    def perform_unfreeze(self) -> None: ...

class RollbackException(BaseException):
    checkpoints: int
    label: str | None
    greedy: bool
    on_load: bool
    abnormal: bool
    current_label: str | None
    def __init__(
        self,
        checkpoints: int,
        label: str | None = None,
        greedy: bool = True,
        on_load: bool = False,
        abnormal: bool = True,
        current_label: str | None = None,
    ) -> None: ...
    def perform_rollback(self) -> None: ...
