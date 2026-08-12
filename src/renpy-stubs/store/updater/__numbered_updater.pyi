import io
import threading
from typing import Any

from renpy.exports import fsencode as fsencode
from renpy.store import DictEquality
from renpy.ui import Action

_constant: bool

def urlopen(url: str) -> io.BytesIO: ...
def urlretrieve(url: str, fn: str) -> None: ...

class UpdateError(Exception): ...
class UpdateCancelled(Exception): ...

class Updater(threading.Thread):
    ERROR: str
    CHECKING: str
    UPDATE_NOT_AVAILABLE: str
    UPDATE_AVAILABLE: str
    PREPARING: str
    DOWNLOADING: str
    UNPACKING: str
    FINISHING: str
    DONE: str
    DONE_NO_RESTART: str
    CANCELLED: str
    patch: bool
    state: str
    message: str | None
    progress: float | None
    can_cancel: bool
    can_proceed: bool
    cancelled: bool
    proceeded: bool
    url: str
    force: bool
    add: list[str]
    restart: bool
    check_only: bool
    confirm: bool
    allow_empty: bool
    done_pause: bool
    allow_cancel: bool
    new_disk_size: int
    old_disk_size: int
    download_total: int
    download_done: int
    write_total: int
    write_done: int
    base: str | None
    updatedir: str
    app: str | None
    condition: str | None
    modules: list[str]
    moves: list[tuple[str, str]]
    public_key: str | None
    log: list[str]
    simulate: bool | None
    daemon: bool
    def __init__(
        self,
        url: str,
        base: str | None = None,
        force: bool = False,
        public_key: str | None = None,
        simulate: bool | None = None,
        add: list[str] = [],
        restart: bool = True,
        check_only: bool = False,
        confirm: bool = True,
        patch: bool = True,
        prefer_rpu: bool = True,
        size_only: bool = False,
        allow_empty: bool = False,
        done_pause: bool = True,
        allow_cancel: bool = True,
    ) -> None: ...
    def run(self) -> None: ...
    pretty_version: str | None
    new_state: str
    def update(self) -> None: ...
    version: str | None
    def prompt_confirm(self) -> None: ...
    def fetch_files_rpu(self, module: str) -> list[str]: ...
    old_disk_total: int
    new_disk_total: int
    def rpu_copy_fields(self) -> None: ...
    def rpu_progress(self, state: str, progress: float | None) -> None: ...
    u: Any | None
    def rpu_update(self) -> None: ...
    def simulation(self) -> None: ...
    def periodic(self) -> float | None: ...
    def proceed(self, force: bool = False) -> None: ...
    def cancel(self) -> None: ...
    def unlink(self, path: str) -> None: ...
    def rename(self, old: str, new: str) -> None: ...
    def path(self, name: str) -> str: ...
    current_state: str
    def load_state(self) -> None: ...
    def test_write(self) -> None: ...
    updates: list[tuple[str, str, str]]

    def add_dlc_state(self, name: str) -> None: ...
    def check_versions(self) -> bool: ...
    def save_state(self) -> None: ...
    def clean(self, fn: str) -> None: ...
    def clean_old(self) -> None: ...

installed_state_cache: dict[str, Any] | None

def get_installed_state(base: str | None = None) -> dict[str, Any]: ...
def get_installed_packages(base: str | None = None) -> list[str]: ...
def can_update(base: str | None = None) -> bool: ...
def update(
    url,
    base: str | None = None,
    force: bool = False,
    public_key: str | None = None,
    simulate: bool | None = None,
    add: list[str] = [],
    restart: bool = True,
    confirm: bool = True,
    patch: bool = True,
    prefer_rpu: bool = True,
    allow_empty: bool = False,
    done_pause: bool = True,
    allow_cancel: bool = True,
    screen: str = "updater",
) -> None: ...

class Update(Action, DictEquality):
    args: tuple[Any, ...]
    kwargs: dict[str, Any]
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def __call__(self) -> None: ...

checked: bool

def UpdateVersion(url: str, check_interval: float = ..., simulate: bool | None = None, **kwargs: Any) -> Update: ...
def update_command() -> Update: ...

downloader: bool | None
downloader_kwargs: dict[str, Any]

def start_game_download(url: str, **kwargs: Any) -> Updater: ...
def continue_game_download(screen: str = "downloader") -> None: ...
