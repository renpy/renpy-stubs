from _typeshed import Incomplete
from typing import Callable
import io

real_open: Callable[..., io.TextIOWrapper]
report: bool

def replacement_open(*args: Incomplete, **kwargs: Incomplete) -> io.TextIOWrapper: ...
def init_main_thread_open() -> None: ...
