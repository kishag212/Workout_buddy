# llm_client.py

import os
import json
from typing import List
from dotenv import load_dotenv
from openai import OpenAI
from exercises_data import Exercise

load_dotenv()

# Get API key from .env
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_workout_text(
    exercises: List[Exercise],
    minutes: int,
    fitness_level: str,
    goal: str,
    joint_issues: List[str],
) -> str:
    """
    Send exercise data to the LLM and get back a friendly workout description.
    """

    exercise_payload = [
        {
            "name": ex.name,
            "muscle_group": ex.muscle_group,
            "difficulty": ex.difficulty,
            "equipment": ex.equipment,
            "sets": ex.default_sets,
            "reps": ex.default_reps,
            "seconds": ex.default_seconds,
            "cue": ex.cue,
        }
        for ex in exercises
    ]

    system_prompt = (
        "You are Workout Buddy, a gentle, beginner-friendly fitness coach. "
        "Use ONLY the exercises provided in the JSON. "
        "Explain things in simple, plain language. "
        "Be body-positive and encouraging. "
        "Do NOT give medical advice or diagnose anything. "
        "If something sounds risky, remind the user to stop and talk to a doctor or health professional."
    )

    user_content = {
        "minutes": minutes,
        "fitness_level": fitness_level,
        "goal": goal,
        "joint_issues": joint_issues,
        "exercises": exercise_payload,
        "instructions": [
            "1. Start with a short friendly intro using the fitness level and goal.",
            "2. Present the workout as a numbered list.",
            "   For each exercise, include: name, sets+reps or time, how-to, and a simple safety tip.",
            "3. Add 1–2 gentle transition sentences like 'Take a sip of water and move on.'",
            "4. End with a short cool-down suggestion and a positive closing message.",
            "5. Remind the user to stop if anything hurts sharply or feels wrong."
        ],
    }

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": json.dumps(user_content, indent=2)},
    ]

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=messages,
        temperature=0.6,
    )

    return response.choices[0].message.content
