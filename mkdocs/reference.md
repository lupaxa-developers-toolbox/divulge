# Reference

Public names are exported from `lupaxa.divulge`.

## Package

| Name                          | Description                                |
| ----------------------------- | ------------------------------------------ |
| `__version__`                 | Package version string                     |
| `get_version()`               | Return `__version__`                       |
| `configure(**options)`        | Update the shared default engine           |
| `info(message, **options)`    | Print at info on stdout                    |
| `success(message, **options)` | Print at success on stdout                 |
| `warning(message, **options)` | Print at warning on stderr                 |
| `error(message, **options)`   | Print at error on stderr                   |
| `system(message, **options)`  | Print at system on stdout                  |
| `Divulge(value)`              | Chainable wrapper around one value         |
| `divulge(value)`              | Sugar helper that returns a `Divulge`      |
| `DivulgeConfig`               | Dataclass of defaults                      |
| `DEFAULT_TIME_FORMAT`         | `"%Y-%m-%d %H:%M:%S %z"`                   |

There is no console script and no `python -m lupaxa.divulge` entry point.

## Levels

| Function  | Stream | Default prefix | Default colour |
| --------- | ------ | -------------- | -------------- |
| `info`    | stdout | `[ Info ]`     | `light_cyan`   |
| `success` | stdout | `[ Success ]`  | `light_green`  |
| `warning` | stderr | `[ Warning ]`  | `light_yellow` |
| `error`   | stderr | `[ Error ]`    | `light_red`    |
| `system`  | stdout | `[ System ]`   | `dark_grey`    |

## Divulge

| Method               | Description                             |
| -------------------- | --------------------------------------- |
| `info(**options)`    | Print `value` at info; return self      |
| `success(**options)` | Print `value` at success; return self   |
| `warning(**options)` | Print `value` at warning; return self   |
| `error(**options)`   | Print `value` at error; return self     |
| `system(**options)`  | Print `value` at system; return self    |
| `warn`               | Alias of `warning`                      |
| `ok`                 | Alias of `success`                      |

## DivulgeConfig

| Field            | Default               |
| ---------------- | --------------------- |
| `error_colour`   | `"light_red"`         |
| `error_prefix`   | `"[ Error ]"`         |
| `warning_colour` | `"light_yellow"`      |
| `warning_prefix` | `"[ Warning ]"`       |
| `success_colour` | `"light_green"`       |
| `success_prefix` | `"[ Success ]"`       |
| `info_colour`    | `"light_cyan"`        |
| `info_prefix`    | `"[ Info ]"`          |
| `system_colour`  | `"dark_grey"`         |
| `system_prefix`  | `"[ System ]"`        |
| `use_colours`    | `True`                |
| `use_prefixes`   | `True`                |
| `use_bold`       | `False`               |
| `time_format`    | `DEFAULT_TIME_FORMAT` |

`configure()` and per-call options use these field names. Per-call aliases
`colour` / `color` and `prefix` map onto the active level.

## Message coercion

| Value type | Printed as                                      |
| ---------- | ----------------------------------------------- |
| `str`      | The string                                      |
| `datetime` | `value.strftime(time_format)`                   |
| other      | `pprint.pformat(value, width=80, compact=True)` |

Whitespace-only results are not printed.

## Colour names

Colours are [termcolor](https://pypi.org/project/termcolor/) names. Common
values include `light_red`, `light_yellow`, `light_green`, `light_cyan`,
`light_blue`, `dark_grey`, `white`, and `magenta`. The engine paints with
`force_color=True` so `use_colours` controls colour, not TTY detection.
Bold is off by default (`use_bold=False`).
