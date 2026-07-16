# Sort Records

Implement `sort_records(records)` in `/app/solution.py`. Plain Python only; the
standard library is fine.

`records` is a list of dicts, each with keys `name` (str), `dept` (str), and
`salary` (int). Return a **new list** of the same records sorted by:

1. `dept` ascending (A–Z).
2. Within the same `dept`, `salary` **descending** (highest first).
3. Records equal on both `dept` and `salary` keep their original input order
   (stable).

Do not mutate the input list.

Example:

```
[
  {"name": "Ann", "dept": "eng",   "salary": 100},
  {"name": "Bob", "dept": "sales", "salary": 90},
  {"name": "Cy",  "dept": "eng",   "salary": 120},
]
->
[
  {"name": "Cy",  "dept": "eng",   "salary": 120},
  {"name": "Ann", "dept": "eng",   "salary": 100},
  {"name": "Bob", "dept": "sales", "salary": 90},
]
```

## What `/app/solution.py` must define

- `sort_records(records)`: takes the list, returns the sorted list.

A sample smoke test is provided at `/app/test_visible.py`
(`python3 /app/test_visible.py`). Passing it is necessary but **not
sufficient** — your function is graded on the full spec above, over inputs not
shown here.
