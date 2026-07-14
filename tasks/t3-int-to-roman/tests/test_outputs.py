import sys

import pytest

sys.path.insert(0, "/app")
import solution

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
