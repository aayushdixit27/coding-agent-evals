import sys

sys.path.insert(0, "/app")
import solution

UsageError = solution.UsageError


# --- resolution: nothing supplied falls back to defaults ---

def test_neither_supplied_uses_defaults():
    assert solution.resolve([], {}) == {"mode": "fast", "preset": "balanced"}


def test_default_does_not_count_as_supplied():
    # The named trap: defaults present on both options must NOT read as a conflict.
    solution.resolve([], {})  # must not raise


# --- one option supplied, various sources: allowed ---

def test_only_mode_flag_ok():
    r = solution.resolve(["--mode", "slow"], {})
    assert r["mode"] == "slow" and r["preset"] == "balanced"


def test_only_preset_flag_ok():
    r = solution.resolve(["--preset", "tiny"], {})
    assert r["preset"] == "tiny" and r["mode"] == "fast"


def test_equals_form():
    assert solution.resolve(["--mode=slow"], {})["mode"] == "slow"


def test_mode_from_env_ok():
    r = solution.resolve([], {"APP_MODE": "slow"})
    assert r["mode"] == "slow" and r["preset"] == "balanced"


def test_flag_beats_env():
    assert solution.resolve(["--mode", "slow"], {"APP_MODE": "fast"})["mode"] == "slow"


# --- two options supplied: must conflict ---

def test_both_flags_conflict():
    try:
        solution.resolve(["--mode", "slow", "--preset", "tiny"], {})
    except UsageError as e:
        msg = str(e).lower()
        assert "mode" in msg and "preset" in msg
    else:
        assert False, "expected UsageError naming both options"


def test_env_and_flag_conflict():
    # mode via env, preset via flag: both supplied
    try:
        solution.resolve(["--preset", "tiny"], {"APP_MODE": "slow"})
    except UsageError:
        pass
    else:
        assert False, "expected UsageError"


def test_both_env_conflict():
    try:
        solution.resolve([], {"APP_MODE": "slow", "APP_PRESET": "tiny"})
    except UsageError:
        pass
    else:
        assert False, "expected UsageError"


def test_explicit_value_equal_to_default_still_supplied():
    # --mode=fast equals the default value but was still explicitly supplied,
    # so together with --preset it is a real conflict. Catches a naive
    # "differs from default" check as well as the "not-None" check.
    try:
        solution.resolve(["--mode=fast", "--preset", "tiny"], {})
    except UsageError:
        pass
    else:
        assert False, "expected UsageError"


# --- misc surface ---

def test_unknown_option_raises():
    try:
        solution.resolve(["--bogus", "x"], {})
    except UsageError:
        pass
    else:
        assert False, "expected UsageError on unknown option"


def test_help_text_mentions_exclusion():
    h = solution.help_text().lower()
    assert "mutually exclusive" in h
    assert "--mode" in h and "--preset" in h
