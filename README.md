<div align="center">
    <img height=100 src="https://github.com/seyLu/python-template/blob/main/static/icons/python.png" alt="Python Template Icon">
    <h1>Python Template</h1>
    <p>Template Repository for quickly starting a Python project</p>
    <p>
        <img src="https://github.com/seyLu/python-template/actions/workflows/codeql.yaml/badge.svg" alt="Codeql badge">
        <img src="https://github.com/seyLu/python-template/actions/workflows/lint.yaml/badge.svg" alt="Lint badge">
        <a href="https://www.python.org/"><img src="https://img.shields.io/badge/python-3.11+-blue" alt="Python 3.11+ badge"></a>
        <a href="https://peps.python.org/pep-0008/"><img src="https://img.shields.io/badge/code%20style-pep8-orange.svg" alt="PEP8 badge"></a>
        <a href="https://github.com/seyLu/python-template/blob/main/LICENSE"><img src="https://img.shields.io/github/license/seyLu/python-template.svg" alt="MIT License"></a>
    </p>
    <p>
        <a href="https://github.com/seyLu/python-template/issues/new">Report Bug</a>
        ·
        <a href="https://github.com/seyLu/python-template/issues/new">Request Feature</a>
        ·
        <a href="https://github.com/seyLu/python-template/discussions">Ask Question</a>
    </p>
</div>

<br>

### Built-in Python Tooling Features

#### Lint Workflow

- **Ruff** (superfast linter written in rust + configured to use isort)
- **Black** (opinionated formatter)
- **Mypy** (type checking + strict config)

#### Lint pre-commit ([see Setup: pre-commit](#setup-pre-commit))

#### Misc

- **Dependabot for pip and github actions**
    * .github/dependabot.yaml
- **Auto-update pre-commit**
    *  .github/workflows/auto-update-pre-commit.yaml
- **Tooling**
    * pyproject.toml

- **Logging** ([see Usage: logging with logging.ini](#usage-logging-with-loggingini))
    * logging.ini
- **Global Editor Rules**
    * .editorconfig

### Setup: pre-commit

```bash
pip install pre-commit
pre-commit install
```

### Usage: logging with logging.ini

```python
import logging
from logging.config import fileConfig
from pathlib import Path

Path("logs").mkdir(exist_ok=True)
fileConfig("logging.ini")

logging.info("Works as expected.")
```
