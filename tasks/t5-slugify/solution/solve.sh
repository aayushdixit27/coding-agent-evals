#!/bin/bash
set -euo pipefail
cat > /app/solution.py <<'PY'
import re


def slugify(s):
    s = s.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")
PY
echo "wrote /app/solution.py"
