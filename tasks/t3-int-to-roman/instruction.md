# Integer to Roman

Implement `int_to_roman(n)` in `/app/solution.py`. Plain Python only.

Given an integer `n` with `1 <= n <= 3999`, return its Roman numeral as a string,
using standard subtractive notation.

Subtractive notation writes the six subtractive pairs as a smaller symbol before a
larger one, rather than by repeating symbols:

- 4 is `IV`, not `IIII`
- 9 is `IX`
- 40 is `XL`
- 90 is `XC`
- 400 is `CD`
- 900 is `CM`

Examples: `1 -> "I"`, `58 -> "LVIII"`, `1994 -> "MCMXCIV"`.

## What `/app/solution.py` must define

- `int_to_roman(n)`: takes an int in `1..3999`, returns the Roman numeral string.

Your function is graded on a variety of inputs, not just the examples here.
