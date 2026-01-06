from . import common as common, deferred as deferred, download as download
from _typeshed import Incomplete as Incomplete

PREPARING: str
DOWNLOADING: str
UNPACKING: str
FINISHING: str

class UpdateError(Exception): ...

class Plan:
    block: Incomplete
    old_filename: Incomplete
    old_offset: Incomplete
    old_size: Incomplete
    compressed: Incomplete
    new_filename: Incomplete
    new_offset: Incomplete
    new_size: Incomplete
    hash: Incomplete
    def __init__(
        self,
        block: Incomplete,
        old_filename: Incomplete,
        old_offset: Incomplete,
        old_size: Incomplete,
        compressed: Incomplete,
        new_filename: Incomplete,
        new_offset: Incomplete,
        new_size: Incomplete,
        hash: Incomplete,
    ) -> None: ...

class Update:
    url: Incomplete
    targetdir: Incomplete
    oldlists: Incomplete
    newlists: Incomplete
    old_directories: Incomplete
    new_directories: Incomplete
    new_files: Incomplete
    old_files: Incomplete
    block_files: Incomplete
    old_disk_total: int
    new_disk_total: int
    download_total: int
    download_done: int
    write_total: int
    write_done: int
    plan: Incomplete
    destination_filename: Incomplete
    destination_fp: Incomplete
    aggressive_removal: Incomplete
    progress_callback: Incomplete
    removals: set[str]
    updatedir: Incomplete
    blockdir: Incomplete
    deleteddir: Incomplete
    logfile: Incomplete
    def __init__(
        self,
        url: Incomplete,
        newlists: Incomplete,
        targetdir: Incomplete,
        oldlists: Incomplete,
        progress_callback: Incomplete = None,
        logfile: Incomplete = None,
        aggressive_removal: bool = False,
    ) -> None: ...
    def init(self) -> None: ...
    def update(self) -> None: ...
    def progress(self, message: Incomplete, done: Incomplete) -> None: ...
    def log(self, message: Incomplete, *args: Incomplete) -> None: ...
    def delete(self, filename: Incomplete) -> None: ...
    def rename(self, old_filename: Incomplete, new_filename: Incomplete) -> None: ...
    def make_directories(self) -> Incomplete: ...
    def find_incomplete_files(self) -> None: ...
    def write_padding(self) -> None: ...
    def scan_old_files(self) -> None: ...
    def prepare_new_files(self) -> None: ...
    def remove_identical_files(self) -> None: ...
    def create_plan(self) -> Incomplete: ...
    def compute_totals(self) -> None: ...
    def find_removals(self) -> None: ...
    def write_destination(self, filename: Incomplete, offset: Incomplete, data: Incomplete) -> None: ...
    def download_patch_progress(self) -> None: ...
    def download_block_file(self, filename: Incomplete, plan: Incomplete) -> Incomplete: ...
    def execute_file_plan(self, plan: Incomplete) -> None: ...
    def execute_plan(self) -> None: ...
    def create_empty_new_files(self) -> None: ...
    def rename_new_files(self) -> None: ...
    def remove_old_files(self) -> None: ...
    def set_xbit(self) -> None: ...

def main() -> None: ...
