from _typeshed import Incomplete
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

class Editor:
    def begin(self, new_window: bool = False, **kwargs) -> None: ...
    def end(self, **kwargs) -> None: ...
    def open(self, filename, line=None, **kwargs) -> None: ...
    has_projects: bool
    def open_project(self, directory) -> None: ...

class SystemEditor(Editor):
    def open(self, filename, line=None, **kwargs) -> None: ...

editor: Incomplete

def init() -> None: ...
def launch_editor(filenames, line: int = 1, transient: bool = False): ...
