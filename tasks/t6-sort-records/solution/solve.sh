#!/bin/bash
set -euo pipefail
cat > /app/solution.py <<'PY'
def sort_records(records):
    return sorted(records, key=lambda r: (r["dept"], -r["salary"]))
PY
echo "wrote /app/solution.py"
