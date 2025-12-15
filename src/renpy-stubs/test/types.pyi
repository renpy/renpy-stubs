import enum
from typing import Any, TypeAlias

NodeState: TypeAlias = Any
NodeLocation: TypeAlias = tuple[str, int]
Position: TypeAlias = tuple[int | float, int | float]

class RenpyTestException(RuntimeError): ...
class RenpyTestAssertionError(AssertionError): ...
class RenpyTestScreenshotError(RenpyTestException): ...
class RenpyTestTimeoutError(TimeoutError): ...

class HookType(enum.Enum):
    SETUP = "setup"
    BEFORE_TESTSUITE = "before_testsuite"
    BEFORE_TESTCASE = "before_testcase"
    AFTER_TESTCASE = "after_testcase"
    AFTER_TESTSUITE = "after_testsuite"
    TEARDOWN = "teardown"
