from _typeshed import Incomplete as Incomplete

proxies: Incomplete

class FetchError(Exception):
    original_exception: Incomplete
    status_code: Incomplete
    def __init__(self, message, exception=None) -> None: ...

def fetch_pause() -> None: ...
def fetch_requests(url, method, data, content_type, timeout, headers): ...
def fetch_emscripten(url, method, data, content_type, timeout, headers): ...
def fetch(
    url,
    method=None,
    data=None,
    json=None,
    content_type=None,
    timeout: int = 5,
    result: str = "bytes",
    params=None,
    headers={},
): ...
