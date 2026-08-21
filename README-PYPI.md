<!-- markdownlint-disable -->
<p align="center">
  <a href="https://github.com/lupaxa-developers-toolbox">
    <img src="https://raw.githubusercontent.com/the-lupaxa-project/brand-assets/master/logos/organisations/developers-toolbox/readme-logo.png" alt="Project Logo" width="256"/><br/>
  </a>
</p>
<h3 align="center">
  The Lupaxa Developers Toolbox<br />
  Part of The Lupaxa Project
</h3>

<br />

# lupaxa-divulge

Opinionated console messaging helper for Python — coloured, prefixed
`info` / `success` / `warning` / `error` / `system` lines.

Built for scripts and tools used by The Lupaxa Project.

## Features

- Simple functions for common message types: **info**, **success**,
  **warning**, **error**, and **system**
- Optional **colours** (via [termcolor](https://pypi.org/project/termcolor/))
  and **prefixes** (for example `[ Info ]`, `[ System ]`)
- Optional **bold** via `use_bold` (off by default)
- Global configuration and per-call `prefix` / `colour` overrides
- Pretty-prints non-string values and formats `datetime` objects
- Two idioms:
  - Procedural: `divulge.info("message")`
  - Chainable: `Divulge("message").info()`
- Fully typed, linted, formatted, and tested

## Installation

### From PyPI

```bash
pip install lupaxa-divulge
```

### From source (development mode)

```bash
pip install -e ".[dev]"
```

Requires Python 3.10+. Runtime dependency: `termcolor`.

## Usage

```python
import lupaxa.divulge as divulge

divulge.info("Server starting")
divulge.success("Operation completed")
divulge.warning("Disk usage high")
divulge.error("Connection failed")
divulge.system("Starting backup job")

divulge.Divulge("done").success()
divulge.divulge({"id": 1}).warning()
```

Turn colours or prefixes off for the process:

```python
divulge.configure(use_colours=False, use_prefixes=False)
```

Bold is off by default. Enable it for one call or for the process:

```python
divulge.info("this line is bold", use_bold=True)
divulge.configure(use_bold=True)
```

A walkthrough of the API is in `demo.py` in the
[source repository](https://github.com/lupaxa-developers-toolbox/divulge).

## Development

Clone the repository and install with Make:

```bash
make init                # first-time makefile-skills checkout
make python-install-dev  # editable install with [dev]
make python-check        # lint, type-check, and test
make mkdocs-serve        # local docs site
```

Documentation: <https://divulge.thelupaxaproject.org/>.

<a href="https://github.com/the-lupaxa-project">
    <img src="https://raw.githubusercontent.com/the-lupaxa-project/brand-assets/master/logos/components/footer-for-child-orgs.svg" alt="The Lupaxa Project Footer" width="100%" />
</a>
