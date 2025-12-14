# 🏋🏽‍♀️ Workout Buddy Bot — Sprint 0 & Sprint 1

Workout Buddy is a beginner-friendly fitness helper.  
It guides users through a short conversation to create a safe workout plan based on time, goal, and joint considerations.

- **Sprint 0**: Core rule engine, basic CLI, tests, repo scaffolding  
- **Sprint 1**: Bug fixes, improved CLI UX, debug logging, integration testing, and demo readiness  

---

## 📁 Project Structure

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
├─tests/
│   test_rules.py
│   test_integration_main.py
│
└─docs/
    integration-checklist.md

---

## 🎯 Purpose

### Sprint 0 Foundation Includes
- A working CLI program
- A simple rule engine with safe defaults
- Passing unit tests
- Repository scaffolding
- Feature specification
- Issues and Pull Request workflow

### Sprint 1 Expands the Prototype
- Improved CLI experience and input validation
- Debug logging added to `choose_difficulty()`
- End-to-end integration testing
- UX polish with clearer help text and error messages
- Demo preparation and documentation

---

## 🚀 Setup Instructions

### 1) Clone the Repository
git clone https://github.com/kishag212/Workout_buddy.git  
cd Workout_buddy

### 2) Create & Activate a Virtual Environment

Windows (PowerShell)
python -m venv .venv  
.\.venv\Scripts\Activate.ps1  

Mac / Linux
python3 -m venv .venv  
source .venv/bin/activate  

### 3) Install Dependencies
pip install -r requirements.txt  

---

## ⚡ Quick Start (Beginner-Friendly)

Run the Workout Buddy CLI
python -m src.main  

Example Interaction

👋 Welcome to Workout Buddy!  
I'll help you get right for your next date/vacation. Let's Go!!!! 💪🏾🌴✈️

What is your fitness level? (beginner / intermediate / advanced or 'quit'): beginner  
How many minutes do you have? (10 / 20 / 30 or 'quit'): 20  
What is your goal? (weight loss / tone / strength / energy or 'quit'): energy  
Any joint issues? (knees / back / shoulders / none or 'quit'): none  

Output
- A safe, beginner-friendly workout routine
- A supportive coaching message
- Clear guidance with no medical advice

---

## ▶️ Run the Streamlit App (Optional UI)

streamlit run streamlit_app.py  

Note: The Streamlit UI is planned for a future sprint and may not be present in all branches.

---

## 🧠 Rule Behavior

Workout Buddy uses a simple rule-based system:

Minutes | Difficulty  
0–9     | beginner  
10–19   | intermediate  
≥ 20    | user-selected level  

Safe Defaults
- Invalid minutes → beginner
- Invalid fitness level → beginner

---

## 🐞 Sprint 1 Debug Logging

[DEBUG] choose_difficulty called with minutes={minutes} and level={level}

This supports transparency and bug-fix verification.

---

## 🔗 Integration Testing

Sprint 1 includes end-to-end integration testing to validate the full CLI flow.

- Tests user input → rule evaluation → workout output
- Ensures components work together correctly
- All integration tests are passing

Run integration tests:
python -m pytest tests/test_integration_main.py -v

---

## ✨ UX Improvements (Sprint 1)

Error Message Improvements

Before  
Invalid input  

After  
Invalid input. Please enter one of the listed options (example: beginner).

Before  
Please try again  

After  
I didn’t understand that. Please choose 10, 20, or 30 minutes.

Help text throughout the CLI was updated to include clear options and examples for beginner users.

---

## 🧪 Running Tests

python -m pytest -v  

Expected Output  
All tests passed

---

## 🧼 Clean Environment Test

The application was tested in a clean virtual environment using only the documented setup steps.

- Fresh virtual environment created
- Dependencies installed from requirements.txt
- CLI and tests ran successfully

Any blockers encountered are documented in the integration checklist.

---

## 🛡 Responsible AI Use

Workout Buddy is a wellness support tool, not a medical advisor.

- Does not diagnose or treat medical conditions
- Does not replace a doctor or trainer
- Encourages stopping if pain or dizziness occurs
- Avoids storing sensitive health data
- AI output includes safety guardrails

---

## 👥 Team Members

Name | Role  
Kisha Wright | Exercise Data & Workout Logic  
Andre | LLM Integration  
Anthony | Conversation Flow & App Orchestration  

---

## 📚 Team Prompt Library
https://docs.google.com/document/d/1PbPoj3RgTDDBkdwqgznOZV3uzFAMLidruMJTBJzNN1k/edit

---

## 📘 Sprint 0 Feature Spec
https://docs.google.com/document/d/14AFDEA0Cuj4SqaPF0q70zlgN1U4etqK5IehNA9ReHmA/edit

---

## 🐞 Sprint 1 Bugfix Pull Request
https://github.com/kishag212/Workout_buddy/pull/16

---

## 🗂 Issues & Pull Request Workflow

Issues
- Must include an owner
- Must include a due date

Pull Requests
- Created from a feature or bugfix branch
- Must reference an Issue:

Closes #ISSUE_NUMBER

---

## 📝 Contribution Guide

git checkout -b feature/my-change  
git push -u origin feature/my-change  

Open a Pull Request, assign a reviewer, reference an issue, and merge after approval.
