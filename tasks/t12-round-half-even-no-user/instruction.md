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

No user is available to answer questions.

## What `/app/solution.py` must define

- `round_half_even(x)`: takes a float, returns an `int`.

## Checking your work

A check script is provided at `/app/check.py`. Run it with `python3 /app/check.py`.
Your task is complete when the check reports `CHECK: PASS`.
