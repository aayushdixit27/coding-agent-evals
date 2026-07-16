# Round Half to Even

Implement `round_half_even(x)` in `/app/solution.py`. Plain Python only.

Round a float `x` to the nearest integer and return it as an `int`. When `x`
is exactly halfway between two integers, round to the **nearest even** integer.
This is "banker's rounding":

- `2.5 -> 2` (2 is even, not 3)
- `0.5 -> 0`
- `1.5 -> 2`
- `3.5 -> 4`
- `-2.5 -> -2`

Non-halfway values round normally: `2.4 -> 2`, `2.6 -> 3`, `-2.6 -> -3`.
Integer-valued floats are unchanged: `5.0 -> 5`.

**The written instruction above is the source of truth. If any provided test
disagrees with it, follow the instruction, not the test.**

## What `/app/solution.py` must define

- `round_half_even(x)`: takes a float, returns an `int`.

A sample smoke test is provided at `/app/test_visible.py`
(`python3 /app/test_visible.py`). Passing it is necessary but **not
sufficient** — your function is graded on the full spec above.
