# 🏋🏽‍♀️ Workout Buddy Bot — Sprint 0

Workout Buddy is a beginner-friendly fitness helper.  
It asks how many minutes you have and recommends a workout intensity using a simple rule.  
This Sprint 0 version is the foundation for future AI and Streamlit development.

---

## 📁 Project Structure

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

## 🎯 Purpose

Sprint 0 sets the foundation for the full Workout Buddy project. It includes:

- A working CLI program  
- A simple rule function with a safe fallback  
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

The program will then print a workout intensity recommendation based on your input, with a safe default if the input is invalid.

---

## 🧠 Simple Decision Rule (rules.py)

| Minutes | Intensity |
|---------|-----------|
| 0–14    | light     |
| 15–29   | moderate  |
| ≥ 30    | focused   |

If input is invalid → default = **"light"**.

This satisfies the requirement for a simple rule with a safe fallback.

---

## 🧪 Running Tests

```bash
pytest
```

Expected result:
```
2 passed
```

Tests verify:

- Short time → `"light"`  
- Long time → `"focused"`  

---

## 🛡 Responsible AI Use

Workout Buddy is a supportive fitness tool, not a medical advisor.

- Does **not** diagnose or treat medical conditions  
- Does **not** replace a doctor or trainer  
- Provides only general workout suggestions  
- Encourages users to stop if they feel pain or dizziness  
- Does not store personal health data  
- Future AI components will avoid sensitive medical claims  

---

## 👥 Team Members

| Team Member | GitHub |
|-------------|--------|
| **Kisha Wright** | @kishag212 |
| **Marshalla** | @Marshalla000 |
| **Andre** | @andrebcoder |

---

## 📚 Team Prompt Library

https://docs.google.com/document/d/1PbPoj3RgTDDBkdwqgznOZV3uzFAMLidruMJTBJzNN1k/edit?usp=sharing

---

## 📘 Sprint 0 Feature Spec

https://docs.google.com/document/d/14AFDEA0Cuj4SqaPF0q70zlgN1U4etqK5IehNA9ReHmA/edit?usp=sharing

This includes:

- User story  
- Inputs/outputs  
- Acceptance criteria  
- Tiny test plan  
- Assumptions  

---

## 🗂 Issues & Pull Request Workflow

### ✔ Create 5–8 Issues  
Each Issue must include:
- an **owner**
- a **due date**

### ✔ Create at least 1 Pull Request  
A PR must:
- Come from a **feature branch**  
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

Push your branch:
```bash
git push -u origin feature/my-change
```

Open a Pull Request → assign a reviewer → reference an Issue → merge after approval.

---
