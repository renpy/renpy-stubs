from renpy.compat import (
    PY2 as PY2,
    basestring as basestring,
    bchr as bchr,
    bord as bord,
    chr as chr,
    open as open,
    pystr as pystr,
    range as range,
    round as round,
    str as str,
    tobytes as tobytes,
    unicode as unicode,
)

def byte_ranges(ranges): ...
def write_range(f, headers, content): ...
def write_multipart(f, headers, content): ...
def download_ranges(url, ranges, destination, progress_callback=None): ...
def download(url, ranges, destination, progress_callback=None) -> None: ...
