import abc
import collections.abc
import contextlib
import dataclasses
from types import FrameType, TracebackType
from typing import Any, Callable, IO, Iterator, NotRequired, Protocol, TextIO, TypedDict, Unpack

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
    filter_private: bool
    max_group_width: int
    max_group_depth: int
    emit_context: bool
    def __init__(self, **kwargs: Unpack[ExceptionPrintContextKwargs]) -> None: ...
    def should_filter(self, filename: str) -> bool: ...
    @contextlib.contextmanager
    def indent(self) -> collections.abc.Generator[None]: ...
    @abc.abstractmethod
    def getvalue(self) -> Any: ...
    @abc.abstractmethod
    def location(self, filename: str, lineno: int, name: str | None) -> None: ...
    @abc.abstractmethod
    def source_carets(self, line: str, carets: str | None) -> None: ...
    @abc.abstractmethod
    def final_exception_line(self, exc_type: str, text: str | None) -> None: ...
    @abc.abstractmethod
    def string(self, text: str) -> None: ...
    @abc.abstractmethod
    def chain_cause(self) -> None: ...
    @abc.abstractmethod
    def chain_context(self) -> None: ...
    @abc.abstractmethod
    def exceptions_separator(self, index: int, total: int) -> None: ...
    @abc.abstractmethod
    def exceptions_close(self) -> None: ...

CAUSE_MESSAGE: str
CONTEXT_MESSAGE: str

class TextIOExceptionPrintContext(ExceptionPrintContext, metaclass=abc.ABCMeta):
    file: TextIO
    def __init__(self, file: TextIO, **kwargs: Unpack[ExceptionPrintContextKwargs]) -> None: ...
    def getvalue(self) -> Any | None: ...
    def _print(self, text: str = "") -> None: ...
    def string(self, text: str) -> None: ...
    def chain_cause(self) -> None: ...
    def chain_context(self) -> None: ...
    def exceptions_separator(self, index: int, total: int) -> None: ...
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
    LOCATION_COLOR: str
    PRIMARY_CARET_COLOR: str
    SECONDARY_CARET_COLOR: str
    EXCEPTION_TYPE_COLOR: str
    EXCEPTION_VALUE_COLOR: str
    def location(self, filename: str, lineno: int, name: str | None) -> None: ...
    def source_carets(self, line: str, carets: str | None) -> None: ...
    def final_exception_line(self, exc_type: str, text: str | None) -> None: ...

class NonColoredExceptionPrintContext(TextIOExceptionPrintContext):
    @staticmethod
    def _display_width(line: str) -> Iterator[int]: ...
    def location(self, filename: str, lineno: int, name: str | None) -> None: ...
    def source_carets(self, line: str, carets: str | None) -> None: ...
    def final_exception_line(self, exc_type: str, text: str | None) -> None: ...

def MaybeColoredExceptionPrintContext(
    file: TextIO | None = None, **kwargs: Unpack[ExceptionPrintContextKwargs]
) -> ExceptionPrintContext: ...
def normalize_renpy_line_offset(filename: str, linenumber: int, offset: int, line: str) -> int: ...
def _calculate_anchors(frame_summary: FrameSummary) -> list[tuple[int, int]] | None: ...

@dataclasses.dataclass(init=False, repr=False, slots=True)
class FrameSummary:
    name: str
    filename: str
    lineno: int
    colno: int | None
    end_lineno: int
    end_colno: int | None
    locals: dict[str, Any] | None = dataclasses.field(default=None, compare=False)
    _lines: list[str] | None = dataclasses.field(default=None, compare=False)
    _carets: list[str] | None = dataclasses.field(default=None, compare=False)
    _anchors_value: list[tuple[int, int]] | None = dataclasses.field(default=None, compare=False)
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
    def __repr__(self) -> str: ...
    @property
    def line(self) -> str: ...
    @property
    def lines(self) -> Iterator[str]: ...
    @property
    def _anchors(self) -> list[tuple[int, int]] | None: ...
    @property
    def carets(self) -> Iterator[str]: ...
    @property
    def significant_lines(self) -> collections.abc.Generator[int]: ...
    def format(self, ctx: ExceptionPrintContext, /) -> None: ...

class StackSummary(list[FrameSummary]):
    def __init__(self, traceback: TracebackType | None, /) -> None: ...
    @staticmethod
    def _report_traceback(tb: TracebackType) -> list[FrameSummary] | None: ...
    def should_filter(self, ctx: ExceptionPrintContext, /) -> bool: ...
    def format(self, ctx: ExceptionPrintContext, /) -> None: ...

def _safe_string[T](value: T, what: str, func: Callable[[T], str] = ...) -> str: ...
def compute_closest_value(value: str, values: list[str]) -> str | None: ...
def handle_attribute_error(exception: AttributeError) -> str | None: ...
def handle_name_error(exception: NameError) -> str | None: ...
def handle_import_error(exception: ImportError) -> str | None: ...

class TracebackException:
    stack: StackSummary
    _str: str
    __notes__: list[str]
    _is_syntax_error: bool
    _exc_type: type[BaseException]
    _exc_type_qualname: str
    _exc_type_module: str
    filename: str | None
    lineno: int | None
    end_lineno: int | None
    text: str | None
    offset: int | None
    end_offset: int | None
    msg: str
    __suppress_context__: bool
    __cause__: TracebackException | None
    __context__: TracebackException | None
    exceptions: list[TracebackException] | None
    simple: str | None
    full: str | None
    traceback_fn: str | None
    def __init__(self, exception: BaseException, /, _seen=None) -> None: ...
    @property
    def exc_type_str(self) -> str: ...
    def __eq__(self, other: object) -> bool: ...
    def __str__(self) -> str: ...
    def format_exception_only(
        self, ctx: ExceptionPrintContext | None = None, /, *, show_group: bool = False
    ) -> Any: ...
    def _format_syntax_error(self, ctx: ExceptionPrintContext) -> None: ...
    def format(
        self, ctx: ExceptionPrintContext | None = None, /, *, chain: bool = True, show_group: bool = False
    ) -> Any: ...
    def __getitem__(self, pos: int) -> str | None: ...
    def __iter__(self) -> Iterator[str | None]: ...
    def __len__(self) -> int: ...

def open_error_file(fn: str, mode: str) -> tuple[IO, str]: ...
def report_exception(e: Exception, editor: bool = True) -> TracebackException: ...
