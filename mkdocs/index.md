# divulge

Opinionated console messaging for Python — coloured, prefixed `info`,
`success`, `warning`, `error`, and `system` lines.

Install the **`lupaxa-divulge`** package and import the `lupaxa.divulge`
namespace:

```bash
pip install lupaxa-divulge
```

```python
import lupaxa.divulge as divulge

divulge.info("Server starting")
divulge.success("Operation completed")
divulge.warning("Disk usage high")
divulge.error("Connection failed")
divulge.system("Starting backup job")
```

`divulge` is a library only. There is no console script and no
`python -m` entry point.

## Levels

| Level     | Stream | Default prefix | Default colour |
| --------- | ------ | -------------- | -------------- |
| `info`    | stdout | `[ Info ]`     | `light_cyan`   |
| `success` | stdout | `[ Success ]`  | `light_green`  |
| `warning` | stderr | `[ Warning ]`  | `light_yellow` |
| `error`   | stderr | `[ Error ]`    | `light_red`    |
| `system`  | stdout | `[ System ]`   | `dark_grey`    |

Colours come from [termcolor](https://pypi.org/project/termcolor/). Prefixes
and colours can be turned off for the process, or overridden on a single
call. Bold is off by default; pass `use_bold=True` to enable it.

## Next steps

- [Getting started](getting-started.md) — install and first messages
- [Usage](usage.md) — configure, wrappers, and per-call options
- [Reference](reference.md) — public API and config fields
- [Examples](examples.md) — copy-paste recipes
