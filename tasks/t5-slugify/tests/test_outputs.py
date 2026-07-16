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
    ("The Quick Brown Fox", "the-quick-brown-fox"),
    ("Hello, World!", "hello-world"),
    ("double  spaces  here", "double-spaces-here"),
    ("Rock & Roll", "rock-roll"),
    ("already-clean-slug", "already-clean-slug"),
    ("C++", "c"),
    ("  Trim Me  ", "trim-me"),
    ("", ""),
    ("!!!", ""),
    ("Multiple---Hyphens", "multiple-hyphens"),
    ("Mixed_Underscore Case", "mixed-underscore-case"),
]


@pytest.mark.parametrize("raw,expected", CASES)
def test_slugify(raw, expected):
    assert solution.slugify(raw) == expected
