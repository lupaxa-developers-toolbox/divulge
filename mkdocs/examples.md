# Examples

## Direct functions

```python
import lupaxa.divulge as divulge

divulge.info("Information message")
divulge.success("Operation completed")
divulge.warning("This is a warning")
divulge.error("Something went wrong!")
divulge.system("System message")
```

## Disable colours and prefixes

```python
divulge.info("Defaults: prefix and colour on")
divulge.configure(use_colours=False, use_prefixes=False)
divulge.info("Colours and prefixes disabled")
divulge.warning("Warning is also plain")
divulge.configure(use_colours=True, use_prefixes=True)
divulge.info("Colours and prefixes restored")
```

## Bold colour (off by default)

```python
divulge.info("Default: coloured, not bold")
divulge.info("This line is bold", use_bold=True)
divulge.configure(use_bold=True)
divulge.success("Bold enabled for the rest of the process")
divulge.configure(use_bold=False)
```

## Class and sugar helper

```python
from lupaxa.divulge import Divulge

Divulge("Hello from class").info()
Divulge("Operation succeeded").success(prefix="[ OK ]")
Divulge({"a": 1, "b": 2}).warning()

divulge.divulge("From sugar helper").info()
divulge.divulge({"key": "value"}).error()
```

## Chain several levels

The same value is printed once per level:

```python
divulge.divulge("Chained message").info().success().warning().error().system()
```

## Non-string values

```python
from datetime import datetime

data = {"id": 1, "status": "ok", "items": [1, 2, 3]}
divulge.info(data)
divulge.info(datetime.now())
divulge.info(datetime.now(), time_format="%H:%M:%S", prefix="[ TIME ]")
```

## Demo script

From a clone of this repository (not installed with the wheel):

```bash
python demo.py
```
