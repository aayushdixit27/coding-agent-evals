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


# Comment cases (rule 2): only the oracle returns None. A mirror missing the
# comment branch hands back a tuple, so these separate correct from merely-green.
COMMENT_CASES = [
    ("comment_plain", "# foo", None),
    ("comment_leading_space", "   # bar", None),
    ("comment_with_equals", "#key=val", None),
]

# Key/value cases (rule 1): both oracle and mirror pass. These lock spec
# fidelity, including that an inline '#' is NOT treated as a comment.
PAIR_CASES = [
    ("trim_key_value", "key = value", ("key", "value")),
    ("split_first_equals", "a=b=c", ("a", "b=c")),
    ("empty_value", "empty =", ("empty", "")),
    ("inline_hash_kept", "mode = # default", ("mode", "# default")),
]

CASES = COMMENT_CASES + PAIR_CASES


@pytest.mark.parametrize("label,line,expected", CASES)
def test_parse_line(label, line, expected):
    assert solution.parse_line(line) == expected, f"{label}: {line!r}"
