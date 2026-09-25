# Usage

## Module Functions

Import the namespace and call a level function. Each function accepts any
value; strings print as-is, `datetime` values use the configured time format,
and other objects are pretty-printed.

```python
import lupaxa.divulge as divulge
from datetime import datetime

divulge.info("plain text")
divulge.info({"id": 1, "status": "ok"})
divulge.info(datetime.now())
```

`warning` and `error` write to stderr. The other levels write to stdout.

Empty or whitespace-only messages are skipped.

## Global Configuration

`configure()` updates the shared default engine. Only
[`DivulgeConfig`](reference.md#divulgeconfig) field names are applied;
unknown keys are ignored.

```python
divulge.configure(use_colours=False, use_prefixes=False)
divulge.info("plain line")
divulge.configure(use_colours=True, use_prefixes=True)
```

Change a default prefix or colour for the rest of the process:

```python
divulge.configure(info_prefix="[ NOTE ]", system_colour="light_blue")
```

## Wrapper and Sugar

`Divulge` holds one value and prints it when you call a level method. Each
method returns `self`, so you can chain.

```python
from lupaxa.divulge import Divulge

Divulge("Hello from class").info()
Divulge("Operation succeeded").success(prefix="[ OK ]")
Divulge({"a": 1, "b": 2}).warning()
```

`divulge.divulge(...)` is the same wrapper:

```python
divulge.divulge("From sugar helper").info()
divulge.divulge("Chained").info().success().warning().error().system()
```

On `Divulge`, `warn` is an alias of `warning` and `ok` is an alias of
`success`.

## Per-Call Options

Any call accepts the same knobs as `configure()`, plus short aliases:

| Option             | Effect                                                 |
| ------------------ | ------------------------------------------------------ |
| `colour` / `color` | Override this call’s colour                            |
| `prefix`           | Override this call’s prefix                            |
| `use_colours`      | Enable or disable colour for this call                 |
| `use_prefixes`     | Enable or disable the prefix for this call             |
| `use_bold`         | Enable or disable bold for this call (default off)     |
| `time_format`      | `strftime` pattern used when the value is a `datetime` |

Level-specific names such as `info_colour` still work when you pass them
explicitly.

```python
divulge.info(datetime.now(), time_format="%H:%M:%S", prefix="[ TIME ]")
divulge.success("saved", colour="light_green", prefix="[ OK ]")
```

Colour names must be valid [termcolor](https://pypi.org/project/termcolor/)
names (`light_cyan`, `dark_grey`, …). Unknown names print uncoloured.

## Colours

`termcolor` is called with `force_color=True`, so `use_colours` is the switch
that matters — output is not gated on whether stdout looks like a TTY. Bold
is off by default; pass `use_bold=True` on a call or via `configure()`.

`system` defaults to `dark_grey`. That is intentional: system lines sit
behind the other four levels.
