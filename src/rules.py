# rules.py

def choose_difficulty(minutes: int, fitness_level: str) -> str:
    """
    Very simple rule:
    - If time is short (<= 10 min) → beginner
    - If user is advanced AND has 20+ min → advanced
    - Otherwise → intermediate
    Safe default = beginner
    """
    try:
        mins = int(minutes)
    except (TypeError, ValueError):
        return "beginner"

    level = (fitness_level or "").strip().lower()

    if mins <= 10:
        return "beginner"

    if level == "advanced" and mins >= 20:
        return "advanced"

    return "intermediate"

