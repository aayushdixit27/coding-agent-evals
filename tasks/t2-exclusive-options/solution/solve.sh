#!/bin/bash
set -euo pipefail
cat > /app/solution.py <<'PY'
class UsageError(Exception):
    pass

_OPTIONS = {
    "--mode": ("mode", "APP_MODE", "fast"),
    "--preset": ("preset", "APP_PRESET", "balanced"),
}
_GROUP = ("mode", "preset")


def _parse_flags(argv):
    """Return {dest: value} for options given on the command line."""
    supplied = {}
    i = 0
    while i < len(argv):
        tok = argv[i]
        if tok.startswith("--") and "=" in tok:
            name, value = tok.split("=", 1)
            if name not in _OPTIONS:
                raise UsageError("unknown option: %s" % name)
            supplied[_OPTIONS[name][0]] = value
            i += 1
        elif tok in _OPTIONS:
            if i + 1 >= len(argv):
                raise UsageError("option %s requires a value" % tok)
            supplied[_OPTIONS[tok][0]] = argv[i + 1]
            i += 2
        else:
            raise UsageError("unknown option: %s" % tok)
    return supplied


def resolve(argv, env):
    env = env or {}
    flags = _parse_flags(list(argv))
    resolved = {}
    supplied = []
    for name, (dest, envvar, default) in _OPTIONS.items():
        if dest in flags:
            resolved[dest] = flags[dest]
            supplied.append(dest)
        elif envvar in env:
            resolved[dest] = env[envvar]
            supplied.append(dest)
        else:
            resolved[dest] = default
    group_supplied = [d for d in supplied if d in _GROUP]
    if len(group_supplied) > 1:
        raise UsageError(
            "--mode and --preset are mutually exclusive; supply at most one"
        )
    return resolved


def help_text():
    return (
        "Usage: app [--mode VALUE] [--preset VALUE]\n"
        "  --mode    APP_MODE    (default: fast)\n"
        "  --preset  APP_PRESET  (default: balanced)\n"
        "Note: --mode and --preset are mutually exclusive; supply at most one.\n"
    )
PY
echo "wrote /app/solution.py"
