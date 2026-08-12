# renpy-stubs

Type stubs for [Ren'Py](https://github.com/renpy/renpy/) to improve type checking
and editor completions for Ren'Py projects. The eventual goal is to merge into the main project.

Since this package is separate, it may not fully sync with the main repository.
This repository maintains type stubs that may be occasionally merged
with auto-generated stubs from the Ren'Py source code.

This follows the [PEP 561](https://peps.python.org/pep-0561/#stub-only-packages) convention of having stubs in separate package.


## Quick Start

```bash
# Install dependencies
uv sync

# Update stubs using info extracted from Ren'Py source files
python main.py extract

# Inject type annotation from the stubs directly into Ren'Py source files
python main.py inject
```


## Integration with the main Ren'Py Repository

The main Ren'Py repository uses these stubs for
type checking via [Pyright](https://github.com/microsoft/pyright).

### Setup

In the main repository's `pyproject.toml`:

```toml
[tool.pyright]
stubPath = "typings"
```

This tells Pyright to look for stubs in the `typings/` directory. The
`renpy-stubs` directory will be placed inside `typings/`.

### One-Command Setup

The main repository's `setup.py` has a `generate` command that handles stubs.
When you run:

```bash
uv run setup.py generate
```

It will:
1. Clone (or update) the `renpy-stubs` repository into `typings/renpy-stubs/`
2. Install dependencies via `uv sync`
3. Run the stub generation pipeline (`extract`)

Once done, the stubs are immediately ready for Pyright to use

## Dependencies

The project uses [uv](https://docs.astral.sh/uv/) for dependency management.
All dependencies are declared in `pyproject.toml` and installed with `uv sync`.

| Package  | Purpose |
|----------|---------|
| `ruff`   | Formatting + linting |
| `mypy`   | `stubgen`, generates initial stubs from source |
| `pytype` | `merge-pyi`, injects stubs into `.py` files |

## Commands

### extract
```bash
python main.py [--path /path/to/renpy] extract
```

Updates stubs by doing the following:

1. **Runs `stubgen`** -- Generates `.pyi` stubs from the Ren'Py source code.
2. **Merge** -- For each generated stub, if a stub currently exists,
   merges them **per-parameter** (see below). New files are taken as-is.
3. **Cleanup** -- Removes `from renpy.compat import` lines.
4. **Relative imports** -- Regenerates `__init__.pyi` re-export files.
5. **Ruff check** -- Fixes auto-fixable issues (unused imports, etc.).
6. **Ruff format** -- Formats all stubs.

### inject
```bash
python main.py [--path /path/to/renpy] inject [filter1] [filter2] [...]
```

Injects the types from the `.pyi` stubs back into the Ren'Py source `.py` files.
This adds type annotations to the source files directly.

Supplying a `filter` argument will only process files that match any of the filters.

For example: `python main.py inject transform` will match:

- `renpy-stubs\display\transform.pyi`
- `renpy-stubs\store\__numbered_matrixtransform.pyi`
- `renpy-stubs\pygame\transform.pyi`


## Extract Merge Architecture

The extract pipeline uses a per-parameter, per-attribute cherrypick
merge strategy instead of blindly overwriting current stubs.

For each parameter or attribute annotation:

| Current Type | Extracted Type | Result | Why |
|--------------|----------------|--------|-----|
| Specific type | Specific type | **Use extracted** (if different) | Prefer new types |
| Specific type | Any/Incomplete/None | **Keep current** |  |
| Incomplete/None | Specific type | **Use extracted** | More specific type |

A specific type is anything like  `float`, `list[str]`, etc.

### What's protected in current stubs during extract

- **`@overload` decorators** -- Preserved verbatim
- **`TYPE_CHECKING` blocks** -- Preserved, new definitions from gen are added
- **Import structure** -- Current imports are kept; new imports from gen are added only for new symbols
- **Comments and formatting**

### What's Automatically Added

- **New type annotations** -- If the new types replace `Incomplete`/`Any`/`None` in the existing stubs
- **New parameters in function signatures**
- **New symbols** -- Classes, functions, type aliases
- **New `TYPE_CHECKING` definitions**

## Project Structure

```
renpy-stubs/
├── main.py                    # CLI entry point
├── pyproject.toml             # Project config + uv dependencies
├── config.json                # User configuration
├── scripts/
│   ├── cherrypick_pyi.py      # Per-parameter cherrypick merge
│   ├── extract.py             # Stub generation pipeline
│   ├── inject.py              # Merge stubs into .py files
│   ├── relative_imports.py    # Generates __init__.pyi files
│   └── config.py              # Configuration loading
├── src/
│   └── renpy-stubs/
│       ├── atl.pyi            # Module: renpy.atl
│       ├── display/           # Module: renpy.display
│       │   ├── behavior.pyi
│       │   └── ...
│       └── ...
└── temp/                      # Scratch directory (gitignored)
```

## Dev & Contributing

### Pre-commit

```bash
uv sync --group dev
pre-commit install
pre-commit run --all-files
```

### Testing a Merge

```bash
# Test the cherrypick merge on a single file
python -m scripts.cherrypick_pyi src/renpy-stubs/atl.pyi temp/gen/renpy/renpy/atl.pyi temp/atl_merged.pyi

# Verify syntax
python -c "import ast; ast.parse(open('temp/atl_merged.pyi').read()); print('OK')"
```
