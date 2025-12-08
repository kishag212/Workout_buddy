# src/app.py

import argparse
from src.rules import choose_difficulty


def run_cli_with_flags() -> bool:
    """
    Parse CLI flags and print a recommendation.

    Returns True if flags were used, False if we should fall back
    to the interactive mode.
    """
    parser = argparse.ArgumentParser(
        description="Workout Buddy CLI – recommends a workout difficulty based on time and fitness level.",
        epilog="Example: python -m src.app --minutes 20 --level advanced",
    )

    parser.add_argument(
        "--minutes",
        type=int,
        help="How many minutes you have for your workout (e.g., 10, 20, 30).",
    )

    parser.add_argument(
        "--level",
        type=str,
        help="Your fitness level: beginner, intermediate, or advanced.",
    )

    args = parser.parse_args()

    # If either arg is missing, we’ll fall back to interactive mode
    if args.minutes is None or args.level is None:
        return False

    difficulty = choose_difficulty(args.minutes, args.level)

    print("Workout Buddy Recommendation (flags mode)")
    print("----------------------------------------")
    print(f"- Time:   {args.minutes} minutes")
    print(f"- Level:  {args.level.strip().lower()}")
    print(f"=> Suggested difficulty: {difficulty}")
    print("(Always listen to your body! ❤️)")

    return True


def run_interactive():
    print(" Hello from the Workout Buddy CLI!")

    name = input("What's your name? ").strip() or "friend"

    print("How many minutes do you have? (10, 20, 30)")
    minutes_raw = input("> ").strip() or "20"

    print("Select your fitness level:")
    print("1 = beginner")
    print("2 = intermediate")
    print("3 = advanced")
    choice = input("> ").strip()

    level_map = {"1": "beginner", "2": "intermediate", "3": "advanced"}
    fitness_level = level_map.get(choice, "beginner")

    difficulty = choose_difficulty(minutes_raw, fitness_level)

    print()
    print(f"Hi {name}! Based on your inputs:")
    print(f"- Time: {minutes_raw} minutes")
    print(f"- Level: {fitness_level}")
    print(f"I recommend starting with a **{difficulty}** workout today.")
    print("(Always listen to your body! ❤️)")


def main():
    # Try to handle CLI flags first
    used_flags = run_cli_with_flags()

    # If flags were not fully provided, fall back to interactive prompt
    if not used_flags:
        run_interactive()


if __name__ == "__main__":
    main()
