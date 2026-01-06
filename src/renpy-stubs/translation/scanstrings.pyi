from _typeshed import Incomplete as Incomplete

STRING_RE: str
REGULAR_PRIORITIES: Incomplete
COMMON_PRIORITIES: Incomplete

class String:
    filename: Incomplete
    line: Incomplete
    text: Incomplete
    comment: Incomplete
    priority: Incomplete
    sort_key: Incomplete
    launcher_file: Incomplete
    def __init__(self, filename: Incomplete, line: Incomplete, text: Incomplete, comment: Incomplete) -> None: ...

def scan_strings(filename: Incomplete) -> Incomplete: ...
def scan_comments(filename: Incomplete) -> Incomplete: ...
def scan_additional_strings() -> Incomplete: ...
def scan(min_priority: int = 0, max_priority: int = 299, common_only: bool = False) -> Incomplete: ...
