import io
from collections.abc import Callable

real_open: Callable[..., io.TextIOWrapper]
report: bool

def replacement_open(*args: str, **kwargs: Any) -> io.TextIOWrapper: ...
def init_main_thread_open() -> None: ...
