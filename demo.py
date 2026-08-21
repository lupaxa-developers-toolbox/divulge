#!/usr/bin/env python3
"""Demonstrate lupaxa.divulge usage."""

from __future__ import annotations

from datetime import datetime

import lupaxa.divulge as divulge
from lupaxa.divulge import Divulge


def main() -> None:
    print("\n=== 1. Direct function usage ===")
    divulge.info("Information message")
    divulge.success("Operation completed")
    divulge.warning("This is a warning")
    divulge.error("Something went wrong!")
    divulge.system("System message")

    print("\n=== 2. Global configuration ===")
    divulge.info("Defaults: prefix and colour on")
    divulge.configure(use_colours=False, use_prefixes=False)
    divulge.info("Colours and prefixes disabled")
    divulge.warning("Warning is also plain")
    divulge.configure(use_colours=True, use_prefixes=True)
    divulge.info("Colours and prefixes restored")

    print("\n=== 3. Bold colour (off by default) ===")
    divulge.info("Default: coloured, not bold")
    divulge.info("This line is bold", use_bold=True)
    divulge.configure(use_bold=True)
    divulge.success("Bold enabled for the rest of the process")
    divulge.configure(use_bold=False)
    divulge.info("Bold turned off again")

    print("\n=== 4. Divulge class chaining ===")
    Divulge("Hello from class").info()
    Divulge("Operation succeeded").success(prefix="[ OK ]")
    Divulge({"a": 1, "b": 2}).warning()

    print("\n=== 5. Sugar helper (divulge.divulge(...)) ===")
    divulge.divulge("From sugar helper").info()
    divulge.divulge("Also success").success()
    divulge.divulge({"key": "value"}).error()

    print("\n=== 6. Chaining multiple calls ===")
    divulge.divulge("Chained message").info().success().warning().error().system()

    print("\n=== 7. Non-string and datetime values ===")
    data = {"id": 1, "status": "ok", "items": [1, 2, 3]}
    divulge.info(data)
    divulge.info(datetime.now())

    print("\n=== 8. Custom formatting ===")
    divulge.info(datetime.now(), time_format="%H:%M:%S", prefix="[ TIME ]")

    print("\n=== Demo complete ===")


if __name__ == "__main__":
    main()
