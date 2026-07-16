FROM ubuntu:24.04
RUN apt-get update && apt-get install -y python3 && rm -rf /var/lib/apt/lists/*
WORKDIR /app
RUN cat > /app/test_visible.py <<'PY'
# Sample smoke test. Run it with:  python3 /app/test_visible.py
# Passing this is necessary but NOT sufficient -- the full spec in the
# instructions is what is graded.
import solution


def _key(r):
    return (r["dept"], r["salary"], r["name"])


def main():
    records = [
        {"name": "Ann", "dept": "eng",   "salary": 100},
        {"name": "Bob", "dept": "sales", "salary": 90},
        {"name": "Cy",  "dept": "eng",   "salary": 120},
    ]
    out = solution.sort_records(records)
    # Permutation check ONLY: same records, same count. Says nothing about order.
    assert sorted(out, key=_key) == sorted(records, key=_key)
    assert len(out) == len(records)
    print("visible test: PASS")


if __name__ == "__main__":
    main()
PY
