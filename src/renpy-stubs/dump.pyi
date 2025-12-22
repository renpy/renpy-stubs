definitions: list[tuple[str, str, int]]
transforms: list[tuple[str, str, int]]
screens: list[tuple[str, str, int]]
file_exists_cache: dict[str, bool]

def file_exists(fn: str) -> bool: ...

completed_dump: bool

def dump(error: bool) -> None: ...
