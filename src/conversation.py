# -------------------------------
# Quit Logic Helper
# -------------------------------
def check_quit(user_input):
    if user_input.lower() in ["quit", "exit", "q"]:
        print("\n👋 Thanks for using Workout Buddy! Come back soon! 💪🏾🌴✈️")
        exit()


# -------------------------------
# Ask Fitness Level
# -------------------------------
def ask_fitness_level():
    options = ["beginner", "intermediate", "advanced"]

    while True:
        level = input(
            "What is your fitness level? (beginner / intermediate / advanced or 'quit'): "
        ).lower()

        check_quit(level)

        if level in options:
            return level

        print("❗ I don’t understand — please stick to the options.\n")


# -------------------------------
# Ask Minutes
# -------------------------------
def ask_minutes():
    while True:
        minutes = input("How many minutes do you have? (or 'quit'): ")

        check_quit(minutes)

        if minutes.isdigit():
            return int(minutes)

        print("❗ Please enter a number only (example: 10, 20, 30).\n")


# -------------------------------
# Ask Goal
# -------------------------------
def ask_goal():
    options = ["weight loss", "tone", "strength", "energy"]

    while True:
        goal = input(
            "What is your goal? (weight loss / tone / strength / energy or 'quit'): "
        ).lower()

        check_quit(goal)

        if goal in options:
            return goal

        print("❗ I don't understand — stick to the options.\n")


# -------------------------------
# Ask Joint Issues
# -------------------------------
def ask_joint_issues():
    options = ["knees", "back", "shoulders", "none"]

    while True:
        joints = input(
            "Any joint issues? (knees / back / shoulders / none or 'quit'): "
        ).lower()

        check_quit(joints)

        if joints in options:
            return joints

        print("❗ I don’t understand — please stick to the options.\n")
