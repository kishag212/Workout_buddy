import unittest
from src.rules import choose_difficulty


class TestChooseDifficulty(unittest.TestCase):
    def test_short_time_defaults_to_beginner(self):
        self.assertEqual(choose_difficulty(5, "advanced"), "beginner")

    def test_advanced_with_enough_time(self):
        self.assertEqual(choose_difficulty(30, "advanced"), "advanced")

    def test_medium_time_intermediate(self):
        self.assertEqual(choose_difficulty(15, "beginner"), "intermediate")


if __name__ == "__main__":
    unittest.main()

