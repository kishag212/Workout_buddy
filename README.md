# 🏋🏽‍♀️ Workout Buddy Bot
# 🏋🏽‍♀️ Workout Buddy Bot — Sprint 0

Workout Buddy is a beginner-friendly fitness helper.  
It asks how many minutes you have and recommends a workout intensity using a simple rule.  
This is the baseline Sprint 0 version, preparing for future AI and Streamlit development.

---

## 📁 Project Structure

```
Workout_buddy/
│  README.md
│  .gitignore
│  rules.py
│  requirements.txt
│
├─src/
│   app.py
│   conversation.py
│   workout_logic.py
│   exercises_data.py
│   llm_client.py
│   main.py
│
└─tests/
    test_rules.py
```

---

## 🎯 Purpose

Sprint 0 sets the foundation for the full Workout Buddy project. It includes:

- A working CLI program  
- A simple rule function with a safe default  
- Two passing tests  
- Repository scaffolding  
- A Feature Spec  
- Issues + Pull Request workflow  

---

## 🚀 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/kishag212/Workout_buddy.git
cd Workout_buddy
```

### 2. Create + Activate a Virtual Environment
**Windows**
```bash
python -m venv .venv
.\.venv\Scripts\Activate
```

**Mac/Linux**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Sprint 0 CLI

```bash
python -m src.app
```

Expected output:

```
👋 Welcome to Workout Buddy (Sprint 0)!
How many minutes do you have today?
```

---

## 🧠 Simple Decision Rule (rules.py)

| Minutes | Intensity |
|---------|-----------|
| 0–14 | light |
| 15–29 | moderate |
| ≥ 30 | focused |

If input is invalid → default = **"light"**.

---

## 🧪 Running Tests

```bash
pytest
```

Expected result:
```
2 passed
```

---

## 🛡 Responsible AI Use

Workout Buddy is a supportive fitness tool, not a medical advisor.

- Does **not** diagnose or treat medical conditions  
- Does **not** replace a doctor or trainer  
- Only provides general workout suggestions  
- Users should stop if they feel pain or dizziness  
- No personal health data is collected or stored  
- User should use discretion and not follow blindly

---

## 👥 Team Members

| Team Member | GitHub |
|-------------|--------|
| **Kisha Wright** | @kishag212 |
| **Marshalla** | @Marshalla000 |
| **Andre** | @andrebcoder |

---

## 📚 Team Prompt Library

Add your shared prompt library link here:

```
https://YOUR_GOOGLE_DOC_LINK
```

---

## 📘 Sprint 0 Feature Spec

Add your Feature Spec link here:

```
https://YOUR_GOOGLE_DOC_LINK
```

---

## 🗂 Issues & Pull Request Workflow

### ✔ Create 5–8 Issues  
Each Issue must include:
- an **owner**
- a **due date**

### ✔ Create at least 1 Pull Request  
A PR must:
- Come from a feature branch  
- Reference an Issue using:

```
Closes #ISSUE_NUMBER
```

- Be open or merged at submission time  

---

## 📝 Contribution Guide (For Teammates)

Create a feature branch:
```bash
git checkout -b feature/my-change
```

Push the branch:
```bash
git push -u origin feature/my-change
```

Open a Pull Request → assign reviewer → reference Issue → merge after approval.

---

## Purpose
Workout Buddy is a small AI-powered workout helper.  
It asks for your fitness level, time, and any joint issues, then creates a gentle beginner-friendly routine.

## How to Set Up

```bash
git clone https://github.com/kishag212/Workout_buddy.git
cd Workout_buddy
python -m venv .venv
# Windows:
.\.venv\Scripts\Activate
pip install -r requirements.txt
3. Install Dependencies
pip install -r requirements.txt
Install Dependencies
pip install -r requirements.txt

▶️ Running the Sprint 0 CLI

Run:

python -m src.app


Expected output:

👋 Welcome to Workout Buddy (Sprint 0)!
How many minutes do you have today?


Then it prints:

Workout intensity

Fallback to safe default if input is invalid

🧠 Simple Decision Rule (rules.py)

Workout intensity is chosen using this rule:

Minutes	Intensity
0–14	light
15–29	moderate
≥ 30	focused

If input is invalid, default = "light"
This satisfies “simple decision rule with a safe default.”

🧪 Running Tests

Use pytest:

pytest


Expected:

2 passed


Tests verify:

Short time → "light"

Long time → "focused"

🛡 Responsible AI Use

Workout Buddy is a supportive fitness tool, not a medical advisor.

Does not diagnose conditions

Does not replace a personal trainer or doctor

Recommends general workout intensities only

Encourages users to stop if they feel pain or dizziness

No personal health data is stored or transmitted

Future AI components will avoid sensitive medical claims

This fulfills the Responsible AI Use requirement.

👥 Team Members
Team Member	GitHub
Kisha Wright	@kishag212

Marshalla	@Marshalla000

Andre	@andrebcoder

This satisfies: Team names + GitHub handles listed.

📚 Team Prompt Library

👉 Add your link here:
https://YOUR_GOOGLE_DOC_LINK

(This fulfills “Link to Team Prompt Library.”)

📘 Sprint 0 Feature Spec

👉 Add your Feature Spec link here:
https://YOUR_GOOGLE_DOC_LINK

This should include:

User story

Inputs/outputs

Acceptance criteria

Tiny test plan

Assumptions

This fulfills the Feature Spec (15 pts) requirement.

🗂 Issues & Pull Request Workflow (Required for Grading)
✔ You must have 5–8 Issues

Example Issues:

Set up repo structure

Implement rules.py

Implement app.py CLI

Create sprint 0 tests

Write README + Responsible AI Use

Write Sprint 0 Feature Spec

Each Issue must have:

An owner

A due date

✔ You must have at least 1 Pull Request

PR should:

Come from a feature branch

Reference an Issue, e.g.:

Closes #2


Be open or merged at submission time

📝 How Teammates Contribute

Create a branch:

git checkout -b feature/my-change


Push it:

git push -u origin feature/my-change