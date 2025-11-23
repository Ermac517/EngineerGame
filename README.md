EngineerGame
===============

Small Python project with basic problem-solving utilities and a simple CLI.

Quick start
-----------

- Create a virtualenv and install dev deps:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

- Run the CLI:

```bash
python -m engineergame.cli prime 17
python -m engineergame.cli factorial 6
python -m engineergame.cli fib 10
python -m engineergame.cli gcd 48 18
```

Run tests
---------

The package uses a `src/` layout (`src/engineergame`). Because of this, tests that
import `engineergame` may fail with `ModuleNotFoundError` if the package is not
installed or `src` is not on `PYTHONPATH`.

You have two simple options to run tests:

- Install the project in editable mode (recommended for development):

```bash
pip install -e .
pytest -q
```

- Run tests without installing by adding `src` to `PYTHONPATH`:

```bash
PYTHONPATH=src pytest -q
```

```bash
pytest -q
```

License
-------

MIT
