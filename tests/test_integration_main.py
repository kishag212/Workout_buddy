# tests/test_integration_main.py

from src import main as workout_main


def test_main_happy_path(monkeypatch, capsys):
    """
    Full happy path:
    - User picks a valid fitness level
    - Provides minutes, goal, and no joint issues
    - We stub the LLM call so no API key / network is needed
    """

    # Fake user inputs for:
    # ask_fitness_level → "1" (beginner)
    # ask_minutes → "20"
    # ask_goal → "get moving"
    # ask_joint_issues → "" (none)
    inputs = iter([
        "1",            # fitness level
        "20",           # minutes
        "get moving",   # goal
        "",             # joint issues
    ])

    def fake_input(_prompt=""):
        return next(inputs)

    # Patch builtins.input so all conversation functions use our fake answers
    monkeypatch.setattr("builtins.input", fake_input)

    # Stub out the LLM client so the test doesn't call OpenAI
    def fake_generate_workout_text(**kwargs):
        return "This is a fake workout for testing."

    monkeypatch.setattr(workout_main, "generate_workout_text", fake_generate_workout_text)

    # Run the high-level CLI entrypoint
    workout_main.main()

    captured = capsys.readouterr()
    out = captured.out

    # Assert key pieces of behavior
    assert "Welcome to Workout Buddy!" in out
    assert "This is a fake workout for testing." in out


def test_main_no_exercises(monkeypatch, capsys):
    """
    Error / edge path:
    - Force filter_exercises to return an empty list
    - Ensure the CLI shows a kind message instead of crashing
    """

    # We still need inputs for all the questions, even if we force no exercises
    inputs = iter([
        "1",            # fitness level
        "10",           # minutes
        "get moving",   # goal
        "knees",        # joint issues
    ])

    def fake_input(_prompt=""):
        return next(inputs)

    monkeypatch.setattr("builtins.input", fake_input)

    # Force no exercises returned
    def fake_filter_exercises(*args, **kwargs):
        return []

    monkeypatch.setattr(workout_main, "filter_exercises", fake_filter_exercises)

    workout_main.main()

    captured = capsys.readouterr()
    out = captured.out

    assert "couldn't find any exercises" in out.lower()
