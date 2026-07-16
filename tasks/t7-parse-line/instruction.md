# Parse Config Line

Implement `parse_line(line)` in `/app/solution.py`. Plain Python only.

Given a single line from a config file, return a `(key, value)` tuple, or
`None`. Apply these rules:

1. **Comment lines.** If the line's first non-whitespace character is `#`, the
   whole line is a comment: return `None`.
2. **Key/value lines.** Otherwise, split on the **first** `=`. Return
   `(key, value)` with surrounding whitespace stripped from both. Everything
   after the first `=` belongs to the value. A `#` that is *not* the first
   non-whitespace character is an ordinary character and stays part of the
   value.

Notes:
- `a=b=c` -> `("a", "b=c")` (split on the first `=` only).
- `key =` -> `("key", "")` (empty value is a real pair, not `None`).
- `mode = # default` -> `("mode", "# default")` (inline `#` is kept, not a comment).

Examples:

- `"  host =  localhost "` -> `("host", "localhost")`
- `"# comment"` -> `None`
- `"a=b=c"` -> `("a", "b=c")`

## What `/app/solution.py` must define

- `parse_line(line)`: takes one line string, returns a `(key, value)` tuple or
  `None`.

A sample smoke test is provided at `/app/test_visible.py`
(`python3 -m pytest /app/test_visible.py`). Passing it is necessary but **not
sufficient** — your function is graded on the full spec above.
