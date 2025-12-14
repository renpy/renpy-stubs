from _typeshed import Incomplete
from typing import Any, NamedTuple

libexec: str

class _LibExecFinder:
    in_find_spec: bool
    def __init__(self) -> None: ...
    def find_spec(self, fullname: str, path, target=None, /): ...

version_dict: Incomplete
official: bool
nightly: bool
version_name: str
version_only: str

class VersionTuple(NamedTuple):
    major: int
    minor: int
    patch: int
    commit: int

version_tuple: Incomplete
version: str
script_version: int
savegame_suffix: str
bytecode_version: int
windows: bool
macintosh: bool
linux: bool
android: bool
ios: bool
emscripten: bool
experimental: Incomplete
arch: str
mobile: bool
macapp: bool
safe_mode_checked: bool
autoreload: bool
session: dict[str, Any]
backup_blacklist: Incomplete
type_blacklist: Incomplete
name_blacklist: Incomplete

class Backup:
    variables: Incomplete
    objects: Incomplete
    names: Incomplete
    def __init__(self) -> None: ...
    objects_pickle: Incomplete
    def backup(self) -> None: ...
    def backup_module(self, mod) -> None: ...
    def restore(self) -> None: ...

backup: Incomplete

def plog(depth, event, *args) -> None: ...
def import_all() -> None: ...
def post_import() -> None: ...
def issubmodule(sub, module): ...
def reload_all() -> None: ...

store: Any
