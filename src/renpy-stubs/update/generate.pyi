import threading
from typing import BinaryIO
from . import common as common, download as download

class BlockGenerator:
    lock: threading.Lock
    targetdir: str
    seen_hashes: set[str]
    max_rpu_size: int
    blocks: list[common.File]
    filelist: common.FileList | None
    segments: list[common.Segment]
    new_rpu: BinaryIO | None
    def __init__(self, targetdir: str, max_rpu_size: int = ...) -> None: ...
    def path(self, name: str) -> str: ...
    def open_new_rpu(self) -> None: ...
    def close_new_rpu(self) -> None: ...
    def generate_segment(self, f: BinaryIO, seg: common.Segment) -> None: ...
    def generate(
        self, name: str, filelist: common.FileList, progress: download.ProgressCallback | None = None
    ) -> None: ...
