# Slugify

Implement `slugify(s)` in `/app/solution.py`. Plain Python only; the standard
library is fine.

Turn a title string into a URL slug with these rules, applied in order:

1. Lowercase the string.
2. Replace every run of one or more characters that are not ASCII letters or
   digits with a single hyphen `-`.
3. Remove any leading or trailing hyphens.

Examples:

- `"Hello, World!" -> "hello-world"`
- `"The Quick Brown Fox" -> "the-quick-brown-fox"`
- `"  Trim Me  " -> "trim-me"`

A run means consecutive separator characters collapse to one hyphen, not one
hyphen each. An empty string, or a string with no letters or digits, returns `""`.

## What `/app/solution.py` must define

- `slugify(s)`: takes a string, returns the slug string.

Your function is graded on a variety of inputs, not just the examples here.
