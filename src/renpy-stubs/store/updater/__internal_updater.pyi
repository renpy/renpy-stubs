import threading
from typing import Any
from _typeshed import Incomplete

from renpy.exports import fsencode as fsencode
from renpy.ui import Action
from renpy.store import DictEquality

_constant: bool

def urlopen(url: Incomplete) -> Incomplete: ...
def urlretrieve(url: Incomplete, fn: Incomplete) -> None: ...

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
    patch: Incomplete
    state: Incomplete
    message: Incomplete
    progress: Incomplete
    can_cancel: bool
    can_proceed: bool
    cancelled: bool
    proceeded: bool
    url: Incomplete
    force: Incomplete
    add: Incomplete
    restart: Incomplete
    check_only: Incomplete
    confirm: Incomplete
    allow_empty: Incomplete
    done_pause: Incomplete
    allow_cancel: bool
    new_disk_size: Incomplete
    old_disk_size: Incomplete
    download_total: Incomplete
    download_done: Incomplete
    write_total: Incomplete
    write_done: Incomplete
    base: Incomplete
    updatedir: Incomplete
    app: Incomplete
    condition: Incomplete
    modules: Incomplete
    moves: Incomplete
    public_key: Incomplete
    log: Incomplete
    simulate: Incomplete
    daemon: bool
    def __init__(
        self,
        url: Incomplete,
        base: Incomplete = None,
        force: bool = False,
        public_key: Incomplete = None,
        simulate: Incomplete = None,
        add: Incomplete = [],
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
    pretty_version: Incomplete
    new_state: Incomplete
    def update(self) -> None: ...
    version: Incomplete
    def prompt_confirm(self) -> None: ...
    def fetch_files_rpu(self, module: Incomplete) -> Incomplete: ...
    old_disk_total: Incomplete
    new_disk_total: Incomplete
    def rpu_copy_fields(self) -> None: ...
    def rpu_progress(self, state: Incomplete, progress: Incomplete) -> None: ...
    u: Incomplete
    def rpu_update(self) -> None: ...
    def simulation(self) -> None: ...
    def periodic(self) -> Incomplete: ...
    def proceed(self, force: bool = False) -> Incomplete: ...
    def cancel(self) -> Incomplete: ...
    def unlink(self, path: Incomplete) -> None: ...
    def rename(self, old: Incomplete, new: Incomplete) -> None: ...
    def path(self, name: Incomplete) -> Incomplete: ...
    current_state: Incomplete
    def load_state(self) -> None: ...
    def test_write(self) -> None: ...
    updates: Incomplete
    def check_updates(self) -> None: ...
    def add_dlc_state(self, name: Incomplete) -> None: ...
    def check_versions(self) -> Incomplete: ...
    def save_state(self) -> None: ...
    def clean(self, fn: Incomplete) -> None: ...
    def clean_old(self) -> None: ...

installed_state_cache: Incomplete

def get_installed_state(base: Incomplete = None) -> Incomplete: ...
def get_installed_packages(base: Incomplete = None) -> Incomplete: ...
def can_update(base: Incomplete = None) -> Incomplete: ...
def update(
    url,
    base: Incomplete = None,
    force: bool = False,
    public_key: Incomplete = None,
    simulate: Incomplete = None,
    add: Incomplete = [],
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
    args: Incomplete
    kwargs: Incomplete
    def __init__(self, *args: Incomplete, **kwargs: Incomplete) -> None: ...
    def __call__(self) -> None: ...

checked: Incomplete

def UpdateVersion(
    url: Incomplete, check_interval: Incomplete = ..., simulate: Incomplete = None, **kwargs: Incomplete
) -> Incomplete: ...
def update_command() -> Incomplete: ...

downloader: Incomplete
downloader_kwargs: Incomplete

def start_game_download(url: Incomplete, **kwargs: Incomplete) -> Incomplete: ...
def continue_game_download(screen: str = "downloader") -> None: ...
