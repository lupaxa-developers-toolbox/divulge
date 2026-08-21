# Getting started

## Requirements

- Python 3.10 or newer
- `termcolor` 3.0 or newer (installed with the package)

## Install

```bash
python3 -m pip install lupaxa-divulge
```

Then import the namespace:

```python
import lupaxa.divulge as divulge

divulge.info("Ready")
```

The PyPI name is `lupaxa-divulge`. The import path is `lupaxa.divulge`.
`lupaxa` is a namespace package — there is no `lupaxa/__init__.py`.

### From source (development)

Editable install with dev extras (includes the MkDocs pins):

```bash
make init
make python-install-dev
```

Site Markdown lives in `mkdocs/` (not GitHub’s special `docs/` directory).
After makefile-skills are installed:

```bash
make mkdocs-serve
```

## First messages

```python
import lupaxa.divulge as divulge

divulge.info("Server starting")
divulge.success("Operation completed")
divulge.warning("Disk usage high")
divulge.error("Connection failed")
divulge.system("Starting backup job")
```

Wrap a value and print it at one or more levels:

```python
divulge.Divulge("done").success()
divulge.divulge({"id": 1}).warning()
```

A walkthrough of the same API lives in `demo.py` at the repository root
(not shipped in the wheel):

```bash
python demo.py
```

## Makefile helpers

```bash
make init                 # clone makefile-skills into .makefiles/
make python-install-dev   # editable install with [dev]
make python-check         # lint + type + test (via makefile-skills)
make mkdocs-serve         # local docs site
```
