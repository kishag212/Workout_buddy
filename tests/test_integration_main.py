from src import main as workout_main


def test_main_happy_path(monkeypatch, capsys):
    """
    Integration happy path:
    - Valid menu-based inputs
    - LLM call stubbed
    - End-to-end CLI flow runs successfully
    """

    # Inputs MUST match the exact CLI options
    inputs = iter([
        "beginner",   # fitness level
        "20",         # minutes
        "energy",     # goal (valid option)
        "none",       # joint issues (valid option)
    ])

    def fake_input(_prompt=""):
        return next(inputs)

    # Patch all input() calls
    monkeypatch.setattr("builtins.input", fake_input)

    # Stub LLM call so no API is required
    def fake_generate_workout_text(*args, **kwargs):
        return "This is a fake workout for testing."

    monkeypatch.setattr(
        workout_main,
        "generate_workout_text",
        fake_generate_workout_text
    )

    # Run the main CLI entry point
    workout_main.main()

    captured = capsys.readouterr().out

    # Assertions
    assert "Welcome to Workout Buddy" in captured
    assert "fake workout" in captured.lower()


def test_main_no_exercises(monkeypatch, capsys):
    """
    Integration edge case:
    - Force filter_exercises to return no exercises
    - App handles the situation gracefully
    """

    inputs = iter([
        "beginner",   # fitness level
        "10",         # minutes
        "energy",     # goal
        "knees",      # joint issue
    ])

    def fake_input(_prompt=""):
        return next(inputs)

    monkeypatch.setattr("builtins.input", fake_input)

    # Force empty exercise list
    def fake_filter_exercises(*args, **kwargs):
        return []

    monkeypatch.setattr(
        workout_main,
        "filter_exercises",
        fake_filter_exercises
    )

    workout_main.main()

    captured = capsys.readouterr().out.lower()

    # Broad assertion so test is not brittle
    assert "exercise" in captured
