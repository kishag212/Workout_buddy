import streamlit as st

from src.exercises_data import filter_exercises
from src.workout_logic import build_workout_routine
from src.llm_client import generate_workout_text


# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Workout Buddy",
    page_icon="🏋🏽‍♀️",
    layout="wide",
)

# ---------- GLOBAL CSS (NEON THEME) ----------
NEON_CSS = """
<style>
/* Overall app background */
.stApp {
    background: radial-gradient(circle at top left, #111827 0, #020617 40%, #000000 100%);
    color: #F9FAFB;
    font-family: "Montserrat", sans-serif;
}

/* Sidebar styling */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #020617 0%, #020617 40%, #111827 100%);
    border-right: 1px solid rgba(148, 163, 184, 0.4);
}

/* Header bar */
.neon-header {
    padding: 1.2rem 2.5rem;
    border-radius: 18px;
    margin-bottom: 1.6rem;
    background: linear-gradient(90deg, #0f172a, #111827, #0f172a);
    box-shadow: 0 0 25px rgba(59, 130, 246, 0.65);
    border: 1px solid rgba(56, 189, 248, 0.7);
}

/* Main title */
.neon-title {
    font-size: 2.4rem;
    font-weight: 800;
    color: #38bdf8;
    letter-spacing: 0.08em;
}

/* Subtitle */
.neon-subtitle {
    font-size: 1rem;
    color: #e5e7eb;
    opacity: 0.9;
}

/* Section label above workout card */
.section-label {
    font-size: 1.1rem;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #a5b4fc;
    margin-bottom: 0.4rem;
}

/* Workout result card */
.workout-card {
    padding: 1.5rem 1.8rem;
    border-radius: 20px;
    background: radial-gradient(circle at top left, #0b1120 0%, #020617 55%, #000000 100%);
    border: 1px solid rgba(56, 189, 248, 0.6);
    box-shadow:
        0 0 30px rgba(56, 189, 248, 0.5),
        0 0 10px rgba(147, 51, 234, 0.4);
}

/* The markdown inside the card */
.workout-card p, .workout-card li {
    font-size: 0.98rem;
}

/* Buttons */
.stButton > button {
    background: linear-gradient(90deg, #22c55e, #16a34a);
    color: white;
    border-radius: 999px;
    border: none;
    padding: 0.55rem 1.6rem;
    font-weight: 700;
    letter-spacing: 0.06em;
    box-shadow: 0 0 16px rgba(34, 197, 94, 0.6);
}
.stButton > button:hover {
    background: linear-gradient(90deg, #4ade80, #22c55e);
}

/* Info / success / error messages – make them a bit more glassy */
.stAlert {
    border-radius: 14px;
    backdrop-filter: blur(12px);
    background-color: rgba(15, 23, 42, 0.9) !important;
}
</style>
"""
st.markdown(NEON_CSS, unsafe_allow_html=True)

# ---------- HEADER ----------
with st.container():
    st.markdown(
        """
        <div class="neon-header">
            <div class="neon-title">🏋🏽‍♀️ WORKOUT BUDDY</div>
            <div class="neon-subtitle">
                A gentle, AI-powered workout helper for every fitness level.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ---------- LAYOUT: SIDEBAR + MAIN ----------
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

# Two-column layout if you want a little “explanation card” next to the workout
left_col, right_col = st.columns([1.1, 1.9])

with left_col:
    st.markdown(
        """
        <div class="section-label">How it works</div>
        """,
        unsafe_allow_html=True,
    )
    st.write(
        "- Use the controls on the left to tell us your level, time, and equipment.\n"
        "- We filter beginner-safe movements that respect your joints.\n"
        "- Then we build a routine and let the AI coach you through it."
    )

with right_col:
    st.markdown(
        """
        <div class="section-label">Your personalized workout</div>
        """,
        unsafe_allow_html=True,
    )

    if st.button("Generate my workout"):
        with st.spinner("Building a safe, friendly routine…"):

            exercises = filter_exercises(
                fitness_level=fitness_level,
                equipment_allowed=allowed_equipment,
                avoid_joints=joint_issues,
            )

            if not exercises:
                st.error(
                    "We couldn’t find any exercises that match those joint and equipment settings. "
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

                # Put the text inside a neon card
                st.markdown(
                    f"<div class='workout-card'>{workout_text}</div>",
                    unsafe_allow_html=True,
                )

                st.caption(
                    "⚠️ This is not medical advice. Stop if anything hurts sharply or feels wrong, "
                    "and talk to a health professional if you have concerns."
                )
    else:
        st.info(
            "Use the controls in the sidebar, then click **Generate my workout** to get your routine."
        )
