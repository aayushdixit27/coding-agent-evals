import subprocess
import pytest

SOLUTION = "/app/solution.py"

CASES = [
    ("1-3,5", "1 2 3 5"),        # happy path from the instruction
    ("3-5,1,4-6", "1 3 4 5 6"),  # overlap + out of order: kills no-sort / no-dedup
    ("10,2,1-3", "1 2 3 10"),    # numeric vs string sort: kills sort-as-text
    ("5,5,5", "5"),              # duplicate singles: dedup
    ("2-4, 3 , 1", "1 2 3 4"),   # whitespace around commas + dedup across range and single
    ("1,2,", "1 2"),             # trailing comma: kills naive int('') crash
    ("42", "42"),                # single number, no range
    ("", ""),                    # empty input: must print an empty line, not crash
]

def run(inp):
    result = subprocess.run(
        ["python3", SOLUTION, inp],
        capture_output=True, text=True, timeout=10,
    )
    assert result.returncode == 0, (
        f"program exited {result.returncode} on input {inp!r}; stderr: {result.stderr}"
    )
    return result.stdout.strip()

@pytest.mark.parametrize("inp,expected", CASES)
def test_range_expand(inp, expected):
    assert run(inp) == expected, f"failed on input {inp!r}"
