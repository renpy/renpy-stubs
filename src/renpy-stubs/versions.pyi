from typing import TypedDict

class Version:
    branch: str
    semver: tuple[int, int, int]
    name: str
    def __init__(self, branch: str, semver: tuple[int, int, int], name: str) -> None: ...

branch_to_version: dict[str, Version]

class VersionDict(TypedDict):
    semver: tuple[int, int, int, int]
    version: str
    name: str
    branch: str
    official: bool
    nightly: bool
    dirty: bool

def get_vc_version() -> VersionDict | None: ...
def get_git_version(nightly: bool = False) -> VersionDict: ...
def get_version() -> VersionDict: ...
def generate_vc_version(nightly: bool = False) -> VersionDict: ...
def main() -> None: ...
