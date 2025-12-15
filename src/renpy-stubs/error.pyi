import abc
import collections.abc
import contextlib
import dataclasses
from _typeshed import Incomplete as Incomplete
from types import FrameType, TracebackType
from typing import Any, Iterator, NotRequired, Protocol, TextIO, TypedDict, Unpack

class HasReportTraceback(Protocol):
    def report_traceback(self, name: str, last: bool, frame: FrameType) -> list["FrameSummary"] | None: ...

class ExceptionPrintContextKwargs(TypedDict):
    filter_private: NotRequired[bool]
    max_group_width: NotRequired[int]
    max_group_depth: NotRequired[int]
    emit_context: NotRequired[bool]

class ExceptionPrintContext(abc.ABC, metaclass=abc.ABCMeta):
    indent_depth: int
    exception_group_depth: int
    need_close: bool
    filter_private: Incomplete
    max_group_width: Incomplete
    max_group_depth: Incomplete
    emit_context: Incomplete
    def __init__(self, **kwargs: Unpack[ExceptionPrintContextKwargs]) -> None: ...
    def should_filter(self, filename: str) -> bool: ...
    @contextlib.contextmanager
    def indent(self) -> collections.abc.Generator[None]: ...
    @abc.abstractmethod
    def getvalue(self) -> Any: ...
    @abc.abstractmethod
    def location(self, filename: str, lineno: int, name: str | None): ...
    @abc.abstractmethod
    def source_carets(self, line: str, carets: str | None): ...
    @abc.abstractmethod
    def final_exception_line(self, exc_type: str, text: str | None): ...
    @abc.abstractmethod
    def string(self, text: str): ...
    @abc.abstractmethod
    def chain_cause(self): ...
    @abc.abstractmethod
    def chain_context(self): ...
    @abc.abstractmethod
    def exceptions_separator(self, index: int, total: int): ...
    @abc.abstractmethod
    def exceptions_close(self): ...

CAUSE_MESSAGE: str
CONTEXT_MESSAGE: str

class TextIOExceptionPrintContext(ExceptionPrintContext, metaclass=abc.ABCMeta):
    file: Incomplete
    def __init__(self, file: TextIO, **kwargs: Unpack[ExceptionPrintContextKwargs]) -> None: ...
    def getvalue(self): ...
    def string(self, text: str): ...
    def chain_cause(self) -> None: ...
    def chain_context(self) -> None: ...
    def exceptions_separator(self, index: int, total: int): ...
    def exceptions_close(self) -> None: ...

class ANSIColors:
    RESET: str
    BLACK: str
    BLUE: str
    CYAN: str
    GREEN: str
    MAGENTA: str
    RED: str
    WHITE: str
    YELLOW: str
    BOLD_BLACK: str
    BOLD_BLUE: str
    BOLD_CYAN: str
    BOLD_GREEN: str
    BOLD_MAGENTA: str
    BOLD_RED: str
    BOLD_WHITE: str
    BOLD_YELLOW: str
    INTENSE_BLACK: str
    INTENSE_BLUE: str
    INTENSE_CYAN: str
    INTENSE_GREEN: str
    INTENSE_MAGENTA: str
    INTENSE_RED: str
    INTENSE_WHITE: str
    INTENSE_YELLOW: str
    BACKGROUND_BLACK: str
    BACKGROUND_BLUE: str
    BACKGROUND_CYAN: str
    BACKGROUND_GREEN: str
    BACKGROUND_MAGENTA: str
    BACKGROUND_RED: str
    BACKGROUND_WHITE: str
    BACKGROUND_YELLOW: str
    INTENSE_BACKGROUND_BLACK: str
    INTENSE_BACKGROUND_BLUE: str
    INTENSE_BACKGROUND_CYAN: str
    INTENSE_BACKGROUND_GREEN: str
    INTENSE_BACKGROUND_MAGENTA: str
    INTENSE_BACKGROUND_RED: str
    INTENSE_BACKGROUND_WHITE: str
    INTENSE_BACKGROUND_YELLOW: str

class ANSIColoredPrintContext(TextIOExceptionPrintContext):
    LOCATION_COLOR: Incomplete
    PRIMARY_CARET_COLOR: Incomplete
    SECONDARY_CARET_COLOR: Incomplete
    EXCEPTION_TYPE_COLOR: Incomplete
    EXCEPTION_VALUE_COLOR: Incomplete
    def location(self, filename, lineno, name) -> None: ...
    def source_carets(self, line, carets): ...
    def final_exception_line(self, exc_type: str, text: str | None): ...

class NonColoredExceptionPrintContext(TextIOExceptionPrintContext):
    def location(self, filename, lineno, name) -> None: ...
    def source_carets(self, line, carets) -> None: ...
    def final_exception_line(self, exc_type, text) -> None: ...

def MaybeColoredExceptionPrintContext(
    file: TextIO | None = None, **kwargs: Unpack[ExceptionPrintContextKwargs]
) -> ExceptionPrintContext: ...
def normalize_renpy_line_offset(filename: str, linenumber: int, offset: int, line: str): ...

@dataclasses.dataclass(init=False, repr=False, slots=True)
class FrameSummary:
    name: str
    filename: str
    lineno: int
    colno: int | None
    end_lineno: int
    end_colno: int | None
    locals: dict[str, Any] | None = dataclasses.field(default=None, compare=False)
    def __init__(
        self,
        name: str,
        filename: str,
        lineno: int,
        colno: int | None = None,
        end_lineno: int | None = None,
        end_colno: int | None = None,
        text: str | None = None,
        locals: dict[str, Any] | None = None,
    ) -> None: ...
    @property
    def line(self): ...
    @property
    def lines(self) -> Iterator[str]: ...
    @property
    def carets(self) -> Iterator[str]: ...
    @property
    def significant_lines(self) -> collections.abc.Generator[Incomplete]: ...
    def format(self, ctx: ExceptionPrintContext, /): ...

class StackSummary(list[FrameSummary]):
    def __init__(self, traceback: TracebackType | None, /) -> None: ...
    def should_filter(self, ctx: ExceptionPrintContext, /) -> bool: ...
    def format(self, ctx: ExceptionPrintContext, /): ...

def compute_closest_value(value: str, values: list[str]) -> str | None: ...
def handle_attribute_error(exception: AttributeError): ...
def handle_name_error(exception: NameError): ...
def handle_import_error(exception: ImportError): ...

class TracebackException:
    stack: Incomplete
    __notes__: list[str]
    filename: Incomplete
    lineno: Incomplete
    end_lineno: Incomplete
    text: Incomplete
    offset: Incomplete
    end_offset: Incomplete
    msg: Incomplete
    __suppress_context__: Incomplete
    __cause__: TracebackException | None
    __context__: TracebackException | None
    exceptions: list[TracebackException] | None
    simple: str | None
    full: str | None
    traceback_fn: str | None
    def __init__(self, exception: BaseException, /, _seen=None) -> None: ...
    @property
    def exc_type_str(self): ...
    def __eq__(self, other): ...
    def format_exception_only(
        self, ctx: ExceptionPrintContext | None = None, /, *, show_group: bool = False
    ) -> Any: ...
    def format(
        self, ctx: ExceptionPrintContext | None = None, /, *, chain: bool = True, show_group: bool = False
    ) -> Any: ...
    def __getitem__(self, pos): ...
    def __iter__(self): ...
    def __len__(self) -> int: ...

def open_error_file(fn, mode) -> tuple[TextIO, str]: ...
def report_exception(e: Exception, editor: bool = True) -> TracebackException: ...
