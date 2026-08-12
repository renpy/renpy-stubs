import ast
import datetime
import functools
import pickle
from typing import Any, BinaryIO

PROTOCOL: int

def dump_paths(filename: str, **roots: object) -> None: ...
def find_bad_reduction(**roots: object) -> str | None: ...
def make_datetime(cls, *args, **kwargs) -> Any: ...

class Unpickler(pickle.Unpickler):
    date: functools.partial[datetime.date]
    time: functools.partial[datetime.time]
    datetime: functools.partial[datetime.datetime]
    def find_class(self, module: str, name: str) -> Any: ...

def load(f: BinaryIO) -> Unpickler: ...
def loads(s: bytes) -> Any: ...
def dump(o: object, f: BinaryIO, highest: bool = False) -> None: ...
def dumps(o: object, highest: bool = False, bad_reduction_name: str | None = None) -> bytes: ...

REWRITE_NODES: dict[str, type]

class AstFixupTransformer(ast.NodeTransformer):
    def visit_Name(self, node: ast.Name) -> ast.Name | ast.Constant: ...

class CallWrapper(ast.Call):
    def __reduce__(self) -> str | tuple[Any, ...]: ...
    lineno: int
    col_offset: int
    func: ast.expr
    args: list[ast.expr]
    keywords: list[ast.keyword]
    def __setstate__(self, state) -> None: ...

class NumWrapper(ast.Constant):
    def __reduce__(self) -> str | tuple[Any, ...]: ...
    lineno: int
    col_offset: int
    value: ast._ConstantValue
    def __setstate__(self, state) -> None: ...

class StrWrapper(ast.Constant):
    def __reduce__(self) -> str | tuple[Any, ...]: ...
    lineno: int
    col_offset: int
    value: ast._ConstantValue
    def __setstate__(self, state) -> None: ...

class ModuleWrapper(ast.Module):
    def __reduce__(self) -> str | tuple[Any, ...]: ...
    body: list[ast.stmt]
    type_ignores: list[ast.TypeIgnore]
    def __setstate__(self, state) -> None: ...

class ReprWrapper(ast.Call):
    def __reduce__(self) -> str | tuple[Any, ...]: ...
    lineno: int
    col_offset: int
    func: ast.expr
    args: list[ast.expr]
    keywords: list[ast.keyword]
    def __setstate__(self, state) -> None: ...

class ArgumentsWrapper(ast.arguments):
    def __reduce__(self) -> str | tuple[Any, ...]: ...
    posonlyargs: list[ast.arg]
    args: list[ast.arg]
    vararg: ast.arg | None
    kwonlyargs: list[ast.arg]
    kw_defaults: list[ast.expr | None]
    kwarg: ast.arg | None
    defaults: list[ast.expr]
    def __setstate__(self, state): ...

class ParamWrapper(ast.Load):
    def __reduce__(self) -> str | tuple[Any, ...]: ...
