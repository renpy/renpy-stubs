from . import common as common, deferred as deferred, download as download
from typing import BinaryIO, Callable, TextIO

PREPARING: str
DOWNLOADING: str
UNPACKING: str
FINISHING: str

class UpdateError(Exception): ...

class Plan:
    block: bool
    old_filename: str
    old_offset: int
    old_size: int
    compressed: int
    new_filename: str
    new_offset: int
    new_size: int
    hash: str
    def __init__(
        self,
        block: bool,
        old_filename: str,
        old_offset: int,
        old_size: int,
        compressed: int,
        new_filename: str,
        new_offset: int,
        new_size: int,
        hash: str,
    ) -> None: ...

class Update:
    url: str
    targetdir: str
    oldlists: list[common.FileList]
    newlists: list[common.FileList]
    old_directories: list[common.Directory]
    new_directories: list[common.Directory]
    new_files: list[common.File]
    old_files: list[common.File]
    block_files: list[common.File]
    old_disk_total: int
    new_disk_total: int
    download_total: int
    download_done: int
    write_total: int
    write_done: int
    plan: list[Plan]
    destination_filename: str | None
    destination_fp: BinaryIO | None
    aggressive_removal: bool
    progress_callback: Callable[[str, float], None] | None
    removals: set[str]
    updatedir: str
    blockdir: str
    deleteddir: str
    logfile: TextIO | None
    def __init__(
        self,
        url: str,
        newlists: list[common.FileList],
        targetdir: str,
        oldlists: list[common.FileList],
        progress_callback: Callable[[str, float], None] | None = None,
        logfile: TextIO | None = None,
        aggressive_removal: bool = False,
    ) -> None: ...
    def init(self) -> None: ...
    def update(self) -> None: ...
    def progress(self, message: str, done: float) -> None: ...
    def log(self, message: str, *args) -> None: ...
    def delete(self, filename: str) -> None: ...
    def rename(self, old_filename: str, new_filename: str) -> None: ...
    def make_directories(self) -> None: ...
    def find_incomplete_files(self) -> None: ...
    def write_padding(self) -> None: ...
    def scan_old_files(self) -> None: ...
    def prepare_new_files(self) -> None: ...
    def remove_identical_files(self) -> None: ...
    def create_plan(self) -> None: ...
    def compute_totals(self) -> None: ...
    def find_removals(self) -> None: ...
    def write_destination(self, filename: str, offset: int, data: bytes) -> None: ...
    def download_patch_progress(self) -> None: ...
    def download_block_file(self, filename: str, plan: list[Plan]) -> str: ...
    def execute_file_plan(self, plan: list[Plan]) -> None: ...
    def execute_plan(self) -> None: ...
    def create_empty_new_files(self) -> None: ...
    def rename_new_files(self) -> None: ...
    def remove_old_files(self) -> None: ...
    def set_xbit(self) -> None: ...

def main() -> None: ...
