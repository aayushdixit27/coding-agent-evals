FROM ubuntu:24.04
RUN apt-get update && apt-get install -y python3 && rm -rf /var/lib/apt/lists/*
WORKDIR /app
RUN cat > /app/test_visible.py <<'PY'
# Sample smoke test. Passing this is necessary but NOT sufficient --
# the full spec in the instructions is what is graded.
import solution


def test_rounding():
    assert solution.round_half_even(2.4) == 2
    assert solution.round_half_even(2.6) == 3
    assert solution.round_half_even(2.5) == 3
PY
