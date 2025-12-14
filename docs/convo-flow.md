# 🗣 Conversation Flow — Workout Buddy

This document describes how users interact with the Workout Buddy CLI from start to finish.

---

## 🎯 Purpose

The goal of the conversation flow is to collect minimal, beginner-friendly inputs and generate a safe, personalized workout plan with supportive guidance.

---

## 🧑‍💻 Entry Point

- The application starts from `src/main.py`
- The conversation logic is handled in `conversation.py`

---

## 🔄 Conversation Steps

The CLI walks the user through the following steps in order:

### 1. Fitness Level
Prompt:
- `beginner`
- `intermediate`
- `advanced`
- `quit`

Behavior:
- Invalid input triggers an error message and re-prompt
- `quit` exits the program cleanly

---

### 2. Time Available
Prompt:
- `10`
- `20`
- `30`
- `quit`

Behavior:
- Invalid input triggers a clear error message
- Safe defaults are applied if needed

---

### 3. Fitness Goal
Prompt:
- `weight loss`
- `tone`
- `strength`
- `energy`
- `quit`

Behavior:
- Input is validated before continuing

---

### 4. Joint Concerns
Prompt:
- `knees`
- `back`
- `shoulders`
- `none`
- `quit`

Behavior:
- Joint concerns are used to filter unsafe exercises

---

## ⚠️ Error Handling & Validation

- If the user enters invalid input:
  - The app displays a clear error message
  - The same question is re-asked
- Example error message:
  - `❗ I don’t understand — please stick to the options.`

---

## 🧠 Decision Flow

1. Inputs are validated
2. Rule engine determines safe difficulty
3. Workout logic selects exercises
4. AI (if enabled) provides supportive coaching text
5. Final workout plan is displayed to the user

---

## 🛡 Responsible AI Guardrails

- AI does **not** make workout or safety decisions
- Rule-based logic determines difficulty and exercise selection
- AI output is limited to encouragement and explanation
- No medical advice is provided

---

## ✅ Exit Conditions

- User enters `quit`
- Program completes after displaying workout plan
