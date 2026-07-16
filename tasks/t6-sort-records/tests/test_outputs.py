import sys
import os

import pytest

sys.path.insert(0, "/app")
import solution

# grader guard (Day 10): fail loudly if the graded solution is missing or mislocated,
# instead of silently grading a stray file (the Day 9 silent-correctness bug).
assert getattr(solution, "__file__", None) and \
    os.path.realpath(solution.__file__) == os.path.realpath("/app/solution.py"), \
    f"grader guard: expected /app/solution.py, imported {getattr(solution, '__file__', None)!r}"


def _r(name, dept, salary):
    return {"name": name, "dept": dept, "salary": salary}


def _expected(records):
    return sorted(records, key=lambda x: (x["dept"], -x["salary"]))


# Each of these has input order != sorted order, so a do-nothing mirror fails them.
MIXED = [_r("Ann", "eng", 100), _r("Bob", "sales", 90), _r("Cy", "eng", 120), _r("Di", "eng", 100)]
DESC = [_r("A", "eng", 80), _r("B", "eng", 120), _r("C", "eng", 100)]
# Identical dept+salary, different name: exercises stable input-order preservation.
FULLTIES = [_r("Zoe", "eng", 100), _r("Amy", "eng", 100)]
ALREADY = _expected([_r("A", "eng", 120), _r("B", "eng", 90), _r("C", "sales", 50)])
REVERSED = list(reversed(ALREADY))

CASES = [
    ("mixed", MIXED),
    ("desc_within_dept", DESC),
    ("full_ties_stable", FULLTIES),
    ("empty", []),
    ("single", [_r("Solo", "eng", 42)]),
    ("already_sorted", ALREADY),
    ("reverse_sorted", REVERSED),
]


@pytest.mark.parametrize("label,records", CASES)
def test_order(label, records):
    assert solution.sort_records(list(records)) == _expected(records), f"{label}: wrong order"


def test_no_mutation():
    records = [_r("Ann", "eng", 100), _r("Bob", "eng", 120)]
    before = list(records)
    solution.sort_records(records)
    assert records == before, "input list was mutated"
