# src/rules.py

def choose_difficulty(minutes, fitness_level: str) -> str:
    """
    Decide workout difficulty based on available minutes and fitness level.

    Returns one of: "beginner", "intermediate", "advanced".

    Safe default: "beginner" when inputs are missing or invalid.
    """

    # --- Guard clause: minutes must be convertible to int ---
    try:
        mins = int(minutes)
    except (TypeError, ValueError):
        return "beginner"

    # --- Normalization for fitness_level ---
    level = (fitness_level or "").strip().lower()

    valid_levels = {"beginner", "intermediate", "advanced"}
    if level not in valid_levels:
        # Guard clause: invalid fitness level → safe default
        return "beginner"

    # --- Core rule logic (matches the decision table) ---

    # Short time => beginner
    if mins <= 10:
        return "beginner"

    # Advanced user with enough time => advanced
    if level == "advanced" and mins >= 20:
        return "advanced"

    # Otherwise => intermediate
    return "intermediate"

