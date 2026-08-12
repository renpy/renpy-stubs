# renpy-stubs
Type stubs for [Ren'Py](https://github.com/renpy/renpy/) to improve type checking and editor completions for Ren'Py projects.

## Dependencies
- [pytype](https://google.github.io/pytype/) [for merge-pyi]
- [mypy](https://www.mypy-lang.org/) [for stubgen]
- [ruff](https://github.com/astral-sh/ruff)
- tqdm
- pre-commit (recommended, dev)

## Installation
```bash
python -m pip install pytype mypy ruff tqdm pre-commit
```

## Usage
### Generate Stubs
```bash
python main.py generate
```

## Installation
Install the runtime/dev tooling:
```bash
python -m pip install pytype mypy ruff tqdm pre-commit
```

If you use the project's tooling lock (uv), you can sync dev tools and install the pre-commit hook:
```bash
uv sync --group dev
uv run pre-commit install
```

## Usage
Generate stubs from Ren'Py
```bash
python main.py generate
```
Merge stubs into Ren'Py
```bash
python main.py merge
```

## Dev & Contributing
- Install pre-commit (see Installation), then run checks locally:
```bash
uv run pre-commit run --all-files
```
- Or rely on the installed git hook to run checks automatically before commit.

Sample successful pre-commit output:
```
trim trailing whitespace.................................................Passed
check that executables have shebangs.....................................Passed
fix end of files.........................................................Passed
check yaml...............................................................Passed
check toml...............................................................Passed
mixed line ending........................................................Passed
check for case conflicts.................................................Passed
ruff check...............................................................Passed
ruff format..............................................................Passed
uv-lock..................................................................Passed
```
