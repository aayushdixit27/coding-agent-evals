# Exclusive Options

Implement a small, self-contained command-line argument resolver in
`/app/solution.py`. Plain Python only, no third-party libraries.

## The CLI

Your resolver handles exactly two options, each taking a string value:

| Option     | Dest     | Env var       | Default    |
| ---------- | -------- | ------------- | ---------- |
| `--mode`   | `mode`   | `APP_MODE`    | `fast`     |
| `--preset` | `preset` | `APP_PRESET`  | `balanced` |

Each option's value is resolved with this precedence: a command-line flag
beats an environment variable, which beats the default.

Both `--opt value` (two tokens) and `--opt=value` (one token) forms are accepted.

## Mutually exclusive group

`--mode` and `--preset` form a mutually exclusive group: at most one of them may
be supplied by the user. An option counts as supplied only when the user provides
it, either through a command-line flag or through its environment variable. An
option left at its default value is not supplied.

If both options in the group are supplied, raise `UsageError` with a message that
names both conflicting options.

## What `/app/solution.py` must define

- `class UsageError(Exception)`.
- `resolve(argv, env)`: `argv` is a list of argument tokens (like `sys.argv[1:]`);
  `env` is a dict of environment variables. Returns a dict `{"mode": <str>,
  "preset": <str>}` of resolved values. Raises `UsageError` on a group conflict or
  an unknown option.
- `help_text()`: returns a usage string that includes a line stating `--mode` and
  `--preset` are mutually exclusive.

Any token starting with `--` that is not `--mode` or `--preset` raises `UsageError`.

Your resolver is graded on a variety of inputs, not just the examples here.
