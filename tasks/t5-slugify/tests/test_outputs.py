import sys

import pytest

sys.path.insert(0, "/app")
import solution

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
