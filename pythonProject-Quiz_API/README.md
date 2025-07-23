# 🧠 Quiz App (OOP + Tkinter GUI)

This is a simple **quiz application** built using **Object-Oriented Programming (OOP)** principles in Python. It uses `tkinter` for the graphical interface and quizzes users based on a list of True/False questions.

---

## 📁 Project Structure

```

quiz\_app/
├── main.py             # Initializes quiz logic and GUI
├── question\_model.py   # Question class
├── quiz\_brain.py       # Core logic for navigating questions and scoring
├── ui.py               # GUI built using tkinter
├── data.py             # Contains the list of questions (question\_data)
└── README.md           # This file

````

---

## ▶️ How to Run

1. Ensure Python 3.x is installed.
2. Clone or download the repository.
3. Place all `.py` files in the same directory.
4. Run the main script:

```bash
python main.py
````

> The GUI will open and start the quiz automatically.

---

## 🚀 Features

* **Multiple classes** for modular code:

  * `Question`: handles individual questions.
  * `QuizBrain`: manages quiz flow, scoring, and validation.
  * `QuizInterface`: provides the GUI with buttons and dynamic updates.
* **Data-driven**: reads questions from a list (`question_data`).
* **Interactive GUI**: built with `tkinter`.
* Immediate **feedback** on correct/incorrect answers.
* Shows **final score** at the end of the quiz.

---

## 📌 Sample Question Data (`data.py`)

```python
question_data = [
    {"text": "The sky is blue.", "correct_answer": "True"},
    {"text": "2 + 2 = 5", "correct_answer": "False"},
    # Add more questions here
]
```

---

## 📚 Learning Concepts

* OOP in Python
* GUI programming with `tkinter`
* Event-driven design (`command` callbacks)
* MVC-style design for better structure

---

