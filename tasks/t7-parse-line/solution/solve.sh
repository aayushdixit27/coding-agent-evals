#!/bin/bash
set -euo pipefail
cat > /app/solution.py <<'PY'
def parse_line(line):
    if line.lstrip().startswith("#"):
        return None
    key, _, value = line.partition("=")
    return (key.strip(), value.strip())
PY
echo "wrote /app/solution.py"
