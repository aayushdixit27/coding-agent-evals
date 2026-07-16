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

CASES = [
    (1, "I"),
    (4, "IV"),
    (9, "IX"),
    (14, "XIV"),
    (40, "XL"),
    (58, "LVIII"),
    (90, "XC"),
    (400, "CD"),
    (900, "CM"),
    (944, "CMXLIV"),
    (1994, "MCMXCIV"),
    (2023, "MMXXIII"),
    (3888, "MMMDCCCLXXXVIII"),
    (3999, "MMMCMXCIX"),
]


@pytest.mark.parametrize("n,expected", CASES)
def test_int_to_roman(n, expected):
    assert solution.int_to_roman(n) == expected
