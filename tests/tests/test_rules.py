# tests/test_rules.py

from rules import choose_difficulty

def test_short_time_defaults_to_beginner():
    assert choose_difficulty(5, "advanced") == "beginner"

def test_advanced_with_enough_time():
    assert choose_difficulty(30, "advanced") == "advanced"

