<p align="center">
  <a href="https://github.com/lupaxa-developers-toolbox">
    <img src="https://raw.githubusercontent.com/the-lupaxa-project/brand-assets/master/logos/organisations/developers-toolbox/readme-logo.png" alt="Developers Toolbox" />
  </a>
</p>

<h1 align="center">Divulge</h1>

Opinionated console messaging helper for Python — coloured, prefixed
`info` / `success` / `warning` / `error` / `system` lines.

The PyPI name is `lupaxa-divulge`. The import path is `lupaxa.divulge`.
`lupaxa` is a namespace package — there is no `lupaxa/__init__.py`. This
is a library only: there is no console script and no `python -m` entry
point.

## Install

```bash
pip install lupaxa-divulge
```

Requires Python 3.10+. Colours come from
[termcolor](https://pypi.org/project/termcolor/) 3.0+ (installed with the
package).

## Usage

```python
import lupaxa.divulge as divulge
from datetime import datetime

divulge.info("Server starting")
divulge.success("Operation completed")
divulge.warning("Disk usage high")
divulge.error("Connection failed")
divulge.system("Starting backup job")

divulge.info({"id": 1, "status": "ok"})
divulge.info(datetime.now())

divulge.Divulge("done").success()
divulge.divulge({"id": 1}).warning()
divulge.divulge("Chained").info().success()
```

`warning` and `error` write to stderr. The other levels write to stdout.
Empty or whitespace-only messages are skipped. Strings print as-is,
`datetime` values use the configured time format, and other objects are
pretty-printed.

Turn colours or prefixes off for the process. Only `DivulgeConfig` field
names are applied; unknown keys are ignored:

```python
divulge.configure(use_colours=False, use_prefixes=False)
divulge.configure(info_prefix="[ NOTE ]", system_colour="light_blue")
```

Bold is off by default. Enable it for one call or for the process:

```python
divulge.info("this line is bold", use_bold=True)
divulge.configure(use_bold=True)
```

On `Divulge`, `warn` is an alias of `warning` and `ok` is an alias of
`success`. Each level method returns `self`, so you can chain.

A walkthrough of the API is in `demo.py` (not shipped in the wheel):

```bash
python demo.py
```

## Levels

| Level     | Stream | Default prefix | Default colour |
| --------- | ------ | -------------- | -------------- |
| `info`    | stdout | `[ Info ]`     | `light_cyan`   |
| `success` | stdout | `[ Success ]`  | `light_green`  |
| `warning` | stderr | `[ Warning ]`  | `light_yellow` |
| `error`   | stderr | `[ Error ]`    | `light_red`    |
| `system`  | stdout | `[ System ]`   | `dark_grey`    |

`system` is `dark_grey` on purpose so those lines sit behind the other
four. `termcolor` is called with `force_color=True`, so `use_colours` is
the switch that matters — output is not gated on whether stdout looks
like a TTY.

## Options

Any call accepts the same knobs as `configure()`, plus short aliases:

| Option             | Effect                                             |
| ------------------ | -------------------------------------------------- |
| `colour` / `color` | Override this call's colour                        |
| `prefix`           | Override this call's prefix                        |
| `use_colours`      | Enable or disable colour for this call             |
| `use_prefixes`     | Enable or disable the prefix for this call         |
| `use_bold`         | Enable or disable bold for this call (default off) |
| `time_format`      | `strftime` pattern for `datetime` values           |

Level-specific names such as `info_colour` still work when you pass them
explicitly. Colour names must be valid termcolor names (`light_cyan`,
`dark_grey`, …). Unknown names print uncoloured.

```python
divulge.info(datetime.now(), time_format="%H:%M:%S", prefix="[ TIME ]")
divulge.success("saved", colour="light_green", prefix="[ OK ]")
```

`configure()` and per-call options use these `DivulgeConfig` fields:

| Field            | Default                    |
| ---------------- | -------------------------- |
| `error_colour`   | `"light_red"`              |
| `error_prefix`   | `"[ Error ]"`              |
| `warning_colour` | `"light_yellow"`           |
| `warning_prefix` | `"[ Warning ]"`            |
| `success_colour` | `"light_green"`            |
| `success_prefix` | `"[ Success ]"`            |
| `info_colour`    | `"light_cyan"`             |
| `info_prefix`    | `"[ Info ]"`               |
| `system_colour`  | `"dark_grey"`              |
| `system_prefix`  | `"[ System ]"`             |
| `use_colours`    | `True`                     |
| `use_prefixes`   | `True`                     |
| `use_bold`       | `False`                    |
| `time_format`    | `"%Y-%m-%d %H:%M:%S %z"`   |

Public names from `lupaxa.divulge`: `__version__`, `get_version()`,
`configure()`, the five level functions, `Divulge`, `divulge()`,
`DivulgeConfig`, and `DEFAULT_TIME_FORMAT`.

## From Source

```bash
make init
make python-install-dev
make python-check
```

<a href="https://github.com/the-lupaxa-project">
    <img src="https://raw.githubusercontent.com/the-lupaxa-project/brand-assets/master/logos/components/footer-for-child-orgs.svg" alt="The Lupaxa Project Footer" width="100%" />
</a>
