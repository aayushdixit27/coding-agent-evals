#!/bin/bash
set -e
cat > /app/solution.py <<'PYEOF'
import sys

def expand(spec):
    result = set()
    for token in spec.split(","):
        token = token.strip()
        if not token:
            continue
        if "-" in token:
            lo, hi = token.split("-", 1)
            for n in range(int(lo), int(hi) + 1):
                result.add(n)
        else:
            result.add(int(token))
    return sorted(result)

spec = sys.argv[1] if len(sys.argv) > 1 else ""
print(" ".join(str(n) for n in expand(spec)))
PYEOF
