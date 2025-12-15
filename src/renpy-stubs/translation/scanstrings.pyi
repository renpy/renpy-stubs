from _typeshed import Incomplete

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
    def __init__(self, filename, line, text, comment) -> None: ...

def scan_strings(filename): ...
def scan_comments(filename): ...
def scan_additional_strings(): ...
def scan(min_priority: int = 0, max_priority: int = 299, common_only: bool = False): ...
