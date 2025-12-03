# exercises_data.py

from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Exercise:
    id: str
    name: str
    muscle_group: str              # e.g., "legs", "core", "upper body"
    difficulty: str                # "beginner", "intermediate", "advanced"
    equipment: str                 # "none", "chair", "mat", etc.
    joints_to_caution: List[str]   # e.g., ["knees", "back"]
    default_sets: int
    default_reps: Optional[int]    # either reps OR seconds
    default_seconds: Optional[int]
    cue: str                       # short how-to tip


EXERCISES: List[Exercise] = [
    # ----- Beginner -----
    Exercise(
        id="march",
        name="March in Place",
        muscle_group="full body",
        difficulty="beginner",
        equipment="none",
        joints_to_caution=[],
        default_sets=1,
        default_reps=None,
        default_seconds=60,
        cue="Stand tall, lift your knees gently, and swing your arms in a relaxed, comfortable way."
    ),
    Exercise(
        id="chair_squat",
        name="Chair Squat",
        muscle_group="legs",
        difficulty="beginner",
        equipment="chair",
        joints_to_caution=["knees"],
        default_sets=2,
        default_reps=8,
        default_seconds=None,
        cue="Use a sturdy chair, sit down slowly, then stand up by pressing through your heels."
    ),
    Exercise(
        id="glute_bridge",
        name="Glute Bridge",
        muscle_group="legs",
        difficulty="beginner",
        equipment="none",
        joints_to_caution=["back"],
        default_sets=2,
        default_reps=10,
        default_seconds=None,
        cue="Lie on your back, squeeze your glutes, lift your hips up, then lower with control."
    ),
    Exercise(
        id="wall_pushup",
        name="Wall Push-Up",
        muscle_group="upper body",
        difficulty="beginner",
        equipment="wall",
        joints_to_caution=["wrists", "shoulders"],
        default_sets=2,
        default_reps=8,
        default_seconds=None,
        cue="Place hands on the wall at chest height, bend elbows to bring chest toward the wall, then press away."
    ),

    # ----- Intermediate -----
    Exercise(
        id="reverse_lunge",
        name="Reverse Lunge",
        muscle_group="legs",
        difficulty="intermediate",
        equipment="none",
        joints_to_caution=["knees"],
        default_sets=2,
        default_reps=8,
        default_seconds=None,
        cue="Step one foot back, lower into a gentle lunge, then push back to standing."
    ),
    Exercise(
        id="incline_pushup",
        name="Incline Push-Up on Table",
        muscle_group="upper body",
        difficulty="intermediate",
        equipment="table",
        joints_to_caution=["wrists", "shoulders"],
        default_sets=2,
        default_reps=8,
        default_seconds=None,
        cue="Hands on a sturdy table, body in a straight line, lower your chest toward the table, then push back up."
    ),
    Exercise(
        id="dead_bug",
        name="Dead Bug",
        muscle_group="core",
        difficulty="intermediate",
        equipment="mat",
        joints_to_caution=["back"],
        default_sets=2,
        default_reps=8,
        default_seconds=None,
        cue="On your back, arms up and knees bent, slowly lower opposite arm and leg, then switch sides."
    ),

    # ----- Advanced -----
    Exercise(
        id="squat_jump",
        name="Squat Jumps",
        muscle_group="legs",
        difficulty="advanced",
        equipment="none",
        joints_to_caution=["knees"],
        default_sets=3,
        default_reps=8,
        default_seconds=None,
        cue="Do a small squat, then explode into a gentle jump, landing softly with bent knees."
    ),
    Exercise(
        id="plank_full",
        name="Full Plank",
        muscle_group="core",
        difficulty="advanced",
        equipment="mat",
        joints_to_caution=["wrists", "back"],
        default_sets=3,
        default_reps=None,
        default_seconds=30,
        cue="Hold a straight line from head to heels, bracing your core and avoiding sagging hips."
    ),
]


def filter_exercises(
    fitness_level: str = "beginner",
    equipment_allowed: Optional[List[str]] = None,
    avoid_joints: Optional[List[str]] = None,
) -> List[Exercise]:
    """
    Filter exercises by:
    - fitness level (difficulty)
    - equipment allowed
    - joints to avoid
    """

    if equipment_allowed is None:
        equipment_allowed = ["none", "chair", "wall", "mat", "table"]

    if avoid_joints is None:
        avoid_joints = []

    # Map fitness level → allowed difficulties
    if fitness_level == "beginner":
        allowed_difficulties = ["beginner"]
    elif fitness_level == "intermediate":
        allowed_difficulties = ["beginner", "intermediate"]
    else:  # advanced
        allowed_difficulties = ["beginner", "intermediate", "advanced"]

    results: List[Exercise] = []
    for ex in EXERCISES:
        # Equipment filter
        if ex.equipment not in equipment_allowed:
            continue

        # Joint safety filter
        if any(j in ex.joints_to_caution for j in avoid_joints):
            continue

        # Difficulty filter
        if ex.difficulty not in allowed_difficulties:
            continue

        results.append(ex)

    return results
