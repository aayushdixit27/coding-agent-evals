#!/bin/bash
set -euo pipefail
# Python's built-in round() already does round-half-to-even (banker's rounding),
# so this is the correct oracle. It DELIBERATELY fails the visible test on 2.5
# (round(2.5) == 2, spec-correct); that failure is intended, do not "fix" it.
cat > /app/solution.py <<'PY'
def round_half_even(x):
    return round(x)
PY
echo "wrote /app/solution.py"
