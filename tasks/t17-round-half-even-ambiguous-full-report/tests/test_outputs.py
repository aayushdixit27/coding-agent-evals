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


# Expected values are HARDCODED integer literals, computed by hand from the spec
# (round half to even). The verifier must NEVER call round() or any rounding
# function -- doing so would recompute with the exact primitive under test and
# defeat the whole point of the task.
CASES = [
    # Ties: round half to EVEN (the spec). The four marked ties are the ones
    # where banker's diverges from half-up, so they are what kills a
    # floor(x + 0.5) mirror. The unmarked ties land on the same value under
    # both methods -- they validate the spec but do not catch the mirror.
    ("half_0_5",      0.5,  0),   # mirror-killer: half-up gives 1
    ("half_1_5",      1.5,  2),
    ("half_2_5",      2.5,  2),   # mirror-killer: half-up gives 3
    ("half_3_5",      3.5,  4),
    ("half_4_5",      4.5,  4),   # mirror-killer: half-up gives 5
    ("half_neg_0_5", -0.5,  0),
    ("half_neg_1_5", -1.5, -2),   # mirror-killer: half-up gives -1
    ("half_neg_2_5", -2.5, -2),
    # Non-ties: ordinary rounding.
    ("nontie_2_4",    2.4,  2),
    ("nontie_2_6",    2.6,  3),
    ("nontie_neg_2_6", -2.6, -3),
    # Integer-valued floats: unchanged.
    ("int_5",         5.0,  5),
    ("int_0",         0.0,  0),
]


@pytest.mark.parametrize("label,x,expected", CASES)
def test_round_half_even(label, x, expected):
    assert solution.round_half_even(x) == expected, \
        f"{label}: round_half_even({x!r}) should be {expected}"
