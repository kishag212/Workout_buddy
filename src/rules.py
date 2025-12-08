def choose_difficulty(minutes, level):
    # 🔍 Debug log required for assignment
    print(f"[DEBUG] choose_difficulty called with minutes={minutes} and level={level}")

    # Guard clauses (safe fallback)
    if minutes is None or not isinstance(minutes, int) or minutes < 0:
        return "beginner"
    if level not in ["beginner", "intermediate", "advanced"]:
        return "beginner"

    # Rule logic
    if minutes < 10:
        return "beginner"
    elif minutes < 20:
        return "intermediate"
    else:
        return level
