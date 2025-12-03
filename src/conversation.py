# conversation.py

def ask_fitness_level():
    print("What is your fitness level?")
    print("1 = beginner")
    print("2 = intermediate")
    print("3 = advanced")

    choice = input("> ").strip()

    # Default to beginner if nothing is typed
    if not choice:
        return "beginner"

    # Ask again if user types something wrong
    while choice not in ["1", "2", "3"]:
        print("Please type 1, 2, or 3.")
        print("1 = beginner, 2 = intermediate, 3 = advanced")
        choice = input("> ").strip()
        if not choice:
            return "beginner"

    # Convert number to fitness level
    level_map = {
        "1": "beginner",
        "2": "intermediate",
        "3": "advanced"
    }

    return level_map[choice]


def ask_minutes():
    print("How many minutes do you have?")
    print("Options: 10, 20, 30")
    
    raw = input("> ").strip()
    try:
        mins = int(raw)
    except ValueError:
        mins = 20

    if mins not in [10, 20, 30]:
        mins = 20

    return mins


def ask_goal():
    goal = input("What's your goal for today? (e.g., get moving, build strength): ").strip()
    if not goal:
        goal = "get moving and feel better"
    return goal


def ask_joint_issues():
    issues = input(
        "Any joints we should be gentle with? (e.g., knees, back, shoulders). "
        "Type a list separated by commas, or press Enter if none: "
    ).strip().lower()

    if not issues:
        return []

    return [i.strip() for i in issues.split(",")]
