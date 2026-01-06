from _typeshed import Incomplete as Incomplete

proxies: Incomplete

class FetchError(Exception):
    original_exception: Incomplete
    status_code: Incomplete
    def __init__(self, message: Incomplete, exception: Incomplete = None) -> None: ...

def fetch_pause() -> None: ...
def fetch_requests(
    url: Incomplete,
    method: Incomplete,
    data: Incomplete,
    content_type: Incomplete,
    timeout: Incomplete,
    headers: Incomplete,
) -> Incomplete: ...
def fetch_emscripten(
    url: Incomplete,
    method: Incomplete,
    data: Incomplete,
    content_type: Incomplete,
    timeout: Incomplete,
    headers: Incomplete,
) -> Incomplete: ...
def fetch(
    url: Incomplete,
    method: Incomplete = None,
    data: Incomplete = None,
    json: Incomplete = None,
    content_type: Incomplete = None,
    timeout: int = 5,
    result: str = "bytes",
    params: Incomplete = None,
    headers: Incomplete = {},
) -> Incomplete: ...
