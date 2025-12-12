# main.py

from src.conversation import (
    ask_fitness_level,
    ask_minutes,
    ask_goal,
    ask_joint_issues,
)
from src.exercises_data import filter_exercises
from src.workout_logic import build_workout_routine
from src.llm_client import generate_workout_text


def main():
    print("👋 Welcome to Workout Buddy!")
    print("I'll help you get right for your next date/vacation. Let's Go!!!! 💪🏾🌴✈️\n")


    fitness_level = ask_fitness_level()
    minutes = ask_minutes()
    goal = ask_goal()
    joint_issues = ask_joint_issues()

    # You can expand this later if you add more gear
    allowed_equipment = ["none", "chair", "wall", "mat", "table"]

    # Get exercises that fit the user
    exercises = filter_exercises(
        fitness_level=fitness_level,
        equipment_allowed=allowed_equipment,
        avoid_joints=joint_issues,
    )

    if not exercises:
        print("Sorry, I couldn't find any exercises that match your needs.")
        return

    routine = build_workout_routine(
        minutes=minutes,
        exercises=exercises,
        fitness_level=fitness_level,
    )

    print("\n🤖 Generating your workout with AI...\n")

    workout_text = generate_workout_text(
        exercises=routine,
        minutes=minutes,
        fitness_level=fitness_level,
        goal=goal,
        joint_issues=joint_issues,
    )

    print(workout_text)


if __name__ == "__main__":
    main()
