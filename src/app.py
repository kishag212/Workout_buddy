# src/app.py

from rules import choose_difficulty

def main():
    print("👋 Hello from the Workout Buddy CLI!")

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

if __name__ == "__main__":
    main()

