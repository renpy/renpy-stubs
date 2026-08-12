from typing import Any, Literal, overload

from _typeshed import Incomplete

proxies: dict[str, str]

class FetchError(Exception):
    original_exception: Exception | None
    status_code: int | None
    def __init__(self, message: str, exception: Exception | None = None) -> None: ...

def fetch_pause() -> None: ...
def fetch_requests(
    url: str, method: str, data: bytes | None, content_type: str, timeout: float, headers: dict[str, str]
) -> bytes | FetchError | None: ...
def fetch_emscripten(
    url: str, method: str, data: bytes | None, content_type: str, timeout: float, headers: dict[str, str]
) -> bytes | FetchError: ...
@overload
def fetch(
    url: str,
    method: str | None = None,
    data: bytes | None = None,
    json: dict[str, Any] | None = None,
    content_type: str | None = None,
    timeout: float = 5,
    result: Literal["bytes"] = ...,
    params: dict[str, str] | None = None,
    headers: dict[str, str] = {},
) -> bytes: ...
@overload
def fetch(
    url: str,
    method: str | None = None,
    data: bytes | None = None,
    json: dict[str, Any] | None = None,
    content_type: str | None = None,
    timeout: float = 5,
    result: Literal["text"] = ...,
    params: dict[str, str] | None = None,
    headers: dict[str, str] = {},
) -> str: ...
@overload
def fetch(
    url: str,
    method: str | None = None,
    data: bytes | None = None,
    json: dict[str, Any] | None = None,
    content_type: str | None = None,
    timeout: float = 5,
    result: Literal["json"] = ...,
    params: dict[str, str] | None = None,
    headers: dict[str, str] = {},
) -> dict[str, Any]: ...

class FetchProgress:
    data: bytes
    upload_expected: Incomplete
    upload_current: int
    offset: int
    download_expected: int
    download_current: int
    monitoring_download: bool
    def __init__(self, data) -> None: ...
    def __len__(self) -> int: ...
    def read(self, size: int = -1): ...
    def get_progress(self): ...

active_fetch_requests: set[FetchProgress]

def get_fetch_requests_progress() -> float: ...
def get_fetch_emscripten_progress() -> float: ...
def get_fetch_progress() -> float: ...
