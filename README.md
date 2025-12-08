# 🏋🏽‍♀️ Workout Buddy Bot — Sprint 0 & Sprint 1

Workout Buddy is a beginner-friendly fitness helper.  
It asks how many minutes you have and recommends a workout intensity using a simple rule.  

- **Sprint 0**: Create core rule engine + basic CLI + tests  
- **Sprint 1**: Fix logic bugs, add debug logging, improve CLI usage, ensure full test coverage

---

# 📁 Project Structure

```
Workout_buddy/
│  README.md
│  .gitignore
│  requirements.txt
│
├─src/
│   app.py
│   rules.py
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

# 🎯 Purpose

### Sprint 0 Foundation Includes:
- A working CLI program  
- A simple rule function with a safe fallback  
- Passing tests  
- Repository scaffolding  
- Feature Spec document  
- Issues + Pull Request workflow  

### Sprint 1 Expands the Prototype:
- Debug logging added to `choose_difficulty()`  
- Bugfix implementation + verifying correct rule behavior  
- Improved CLI usage examples  
- Updated test results  
- Added PR for bugfix transparency  

---

# 🚀 Setup Instructions

## 1. Clone the Repository
```bash
git clone https://github.com/kishag212/Workout_buddy.git
cd Workout_buddy
```

## 2. Create + Activate a Virtual Environment
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

## 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Workout Buddy CLI

## **Interactive Mode**
```bash
python -m src.app
```

**Example Output:**
```
👋 Welcome to Workout Buddy!
What's your name? >
How many minutes do you have today? >
Recommended workout difficulty: intermediate
```

---

## **Flags Mode (Sprint 1 Requirement)**

```bash
python -m src.app --minutes 25 --level advanced
```

**Example Output:**
```
Workout Buddy Recommendation (flags mode)
----------------------------------------
- Time: 25 minutes
- Level: advanced
=> Suggested difficulty: advanced
(Always listen to your body! ❤️)
```

---

# 🧠 Rule Behavior (Updated for Sprint 1)

Workout Buddy uses a simple rule-based system:

| Minutes | Difficulty |
|---------|------------|
| 0–9     | beginner   |
| 10–19   | intermediate |
| ≥ 20    | user's chosen level ("beginner", "intermediate", "advanced") |

### Safe Defaults
- Invalid minutes (negative, None, wrong type) → `"beginner"`
- Invalid fitness level → `"beginner"`

---

# 🐞 Sprint 1 Debug Log (Required for Assignment)

A debug log is now printed every time the rule runs:

```
[DEBUG] choose_difficulty called with minutes={minutes} and level={level}
```

This improves transparency and supports the “Bug Fix Evidence” requirement.

---

# 🧪 Running Tests

To run tests:

```bash
python -m unittest -v
```

**Expected output:**
```
test_short_time_defaults_to_beginner ... ok
test_medium_time_intermediate ... ok
test_advanced_with_enough_time ... ok
----------------------------------------------------------------------
Ran 3 tests in 0.002s
OK
```

Tests verify:
- Short time → beginner  
- Medium time → intermediate  
- Long time → advanced  
- Invalid inputs → safe defaults  

---

# 🛡 Responsible AI Use

Workout Buddy is a supportive fitness tool, not a medical advisor.

- Does **not** diagnose or treat medical conditions  
- Does **not** replace a doctor or trainer  
- Provides general workout suggestions only  
- Encourages stopping if pain or dizziness occurs  
- Avoids storing personal health data  
- Future AI components will avoid making sensitive medical claims  

---

# 👥 Team Members (Sprint 0 & Sprint 1)

| Team Member | GitHub |
|-------------|--------|
| **Kisha Wright** | @kishag212 |
| **Marshalla** | @Marshalla000 |
| **Andre** | @andrebcoder |

---

# 📚 Team Prompt Library
https://docs.google.com/document/d/1PbPoj3RgTDDBkdwqgznOZV3uzFAMLidruMJTBJzNN1k/edit?usp=sharing

---

# 📘 Sprint 0 Feature Spec
https://docs.google.com/document/d/14AFDEA0Cuj4SqaPF0q70zlgN1U4etqK5IehNA9ReHmA/edit?usp=sharing

---

# 🐞 Sprint 1 Bugfix Pull Request
https://github.com/kishag212/Workout_buddy/pull/16

This PR includes:
- Debug log added  
- Rule verification  
- Passing tests  
- Issue reference  
- Bugfix evidence for Sprint 1 submission  

---

# 🗂 Issues & Pull Request Workflow (Sprint 0 + 1)

### ✔ Issues must include:
- An **owner**
- A **due date**

### ✔ Pull Requests must:
- Come from a feature or bugfix branch  
- Reference an Issue using:
```
Closes #ISSUE_NUMBER
```
- Be open or merged by submission time  

---

# 📝 Contribution Guide

Create a feature branch:
```bash
git checkout -b feature/my-change
```

Push your branch:
```bash
git push -u origin feature/my-change
```

Open a Pull Request → assign a reviewer → reference an Issue → merge after approval.

---

