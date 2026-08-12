from collections.abc import Callable
from typing import Any

import renpy

registry: dict[str, dict[str, Any]]
parsers: renpy.parser.ParseTrie

def register(
    name: str,
    parse: Callable | None = None,
    lint: Callable | None = None,
    execute: Callable | None = None,
    predict: Callable | None = None,
    next: Callable | None = None,
    scry: Callable | None = None,
    block: bool | str = False,
    init: bool = False,
    translatable: bool = False,
    execute_init: Callable | None = None,
    init_priority: int | Callable = 0,
    label: Callable | None = None,
    warp: Callable | None = None,
    translation_strings: Callable | None = None,
    force_begin_rollback: bool = False,
    post_execute: Callable | None = None,
    post_label: Callable | None = None,
    predict_all: bool = True,
    predict_next: Callable | None = None,
    execute_default: Callable | None = None,
    reachable: Callable | None = None,
) -> None: ...
def parse(node: renpy.ast.Node, line: str, subblock: list[Any]) -> tuple[str, Any]: ...
def call(method: str, parsed: tuple[str, Any], *args: Any, **kwargs: Any) -> Any: ...
def get(key: str, parsed: tuple[str, Any]) -> Any: ...
def get_name(parsed: tuple[str, Any]) -> str: ...
