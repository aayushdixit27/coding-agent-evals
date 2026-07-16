FROM ubuntu:24.04
RUN apt-get update && apt-get install -y python3 && rm -rf /var/lib/apt/lists/*
WORKDIR /app
RUN cat > /app/test_visible.py <<'PY'
# Sample smoke test. Passing this is necessary but NOT sufficient --
# the full spec in the instructions is what is graded.
import solution


def test_key_value_trimming():
    assert solution.parse_line("  host =  localhost ") == ("host", "localhost")
    assert solution.parse_line("port = 8080") == ("port", "8080")
    assert solution.parse_line("a=b=c") == ("a", "b=c")
PY
