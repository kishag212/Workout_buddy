import streamlit as st

from src.exercises_data import filter_exercises
from src.workout_logic import build_workout_routine
from src.llm_client import generate_workout_text


st.set_page_config(page_title="Workout Buddy", page_icon="🏋🏽‍♀️", layout="centered")

st.title("🏋🏽‍♀️ Workout Buddy")
st.write("A gentle, AI-powered workout helper for all fitness levels.")


# ---- SIDEBAR: SETTINGS ----
st.sidebar.header("⚙️ Settings")

fitness_level = st.sidebar.radio(
    "Fitness level",
    options=["beginner", "intermediate", "advanced"],
    index=0,
)

minutes = st.sidebar.slider(
    "How many minutes do you have?",
    min_value=10,
    max_value=60,
    value=20,
    step=5,
)

goal = st.sidebar.text_input(
    "Goal for today",
    value="get moving and feel better",
)

joint_issues = st.sidebar.multiselect(
    "Joints to be gentle with",
    options=["knees", "back", "shoulders", "wrists"],
    default=[],
)

allowed_equipment = st.sidebar.multiselect(
    "Equipment you have",
    options=["none", "chair", "wall", "mat", "table"],
    default=["none", "chair", "mat"],
)


st.markdown("---")

st.subheader("✨ Your Personalized Workout")

if st.button("Generate my workout"):
    with st.spinner("Building a safe, friendly routine…"):

        exercises = filter_exercises(
            fitness_level=fitness_level,
            equipment_allowed=allowed_equipment,
            avoid_joints=joint_issues,
        )

        if not exercises:
            st.error(
                "I couldn’t find any exercises that match those joint and equipment settings. "
                "Try allowing more equipment or fewer joint restrictions."
            )
        else:
            routine = build_workout_routine(
                minutes=minutes,
                exercises=exercises,
                fitness_level=fitness_level,
            )

            # Call LLM to write the friendly text
            workout_text = generate_workout_text(
                exercises=routine,
                minutes=minutes,
                fitness_level=fitness_level,
                goal=goal,
                joint_issues=joint_issues,
            )

            st.success(f"Here’s your {minutes}-minute {fitness_level} workout:")
            st.markdown(workout_text)
            st.caption(
                "⚠️ This is not medical advice. Stop if anything hurts sharply or feels wrong, "
                "and talk to a health professional if you have concerns."
            )
else:
    st.info("Use the controls on the left, then click **Generate my workout** to get started.")
