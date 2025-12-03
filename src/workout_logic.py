# workout_logic.py

from typing import List
from exercises_data import Exercise

def build_workout_routine(
    minutes: int,
    exercises: List[Exercise],
    fitness_level: str
) -> List[Exercise]:
    """
    Decide how many exercises to include based on:
    - how much time the user has
    - their fitness level
    """

    # Rough rule: ~2 minutes per exercise
    base_num = max(3, min(6, minutes // 2))

    if fitness_level == "beginner":
        num = base_num
    elif fitness_level == "intermediate":
        num = min(base_num + 1, len(exercises))
    else:  # advanced
        num = min(base_num + 2, len(exercises))

    return exercises[:num]


# Optional helper if anything still calls the old name:
def build_beginner_routine(minutes: int, exercises: List[Exercise]) -> List[Exercise]:
    return build_workout_routine(minutes, exercises, "beginner")
