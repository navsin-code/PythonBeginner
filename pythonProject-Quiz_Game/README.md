
# 🧠 Quiz App (Command-Line Version)

This is a simple **True/False quiz application** written in Python using **Object-Oriented Programming (OOP)** principles. It runs entirely in the command-line interface (CLI).

---

## 📁 Project Structure

```

quiz\_app/
├── main.py             # Main logic to run the quiz
├── question\_model.py   # Defines the Question class
├── quiz\_brain.py       # Handles quiz logic, scoring, and flow
├── data.py             # Contains a list of question dictionaries
└── README.md           # This file

````

---

## ▶️ How to Run

1. Ensure you have Python 3.x installed.
2. Clone or download the repository.
3. Place all the `.py` files in one directory.
4. Run the main script:

```bash
python main.py
````

---

## 🚀 Features

* Loads a list of **True/False** questions from a Python dictionary.
* Uses the `Question` class to encapsulate question text and answers.
* `QuizBrain` class manages:

  * Displaying questions one by one
  * Validating user input
  * Keeping score and tracking question number
* Runs until all questions are answered.
* Displays final score after the quiz ends.

---

## 📌 Sample Question Data (`data.py`)

```python
question_data = [
    {"question": "The sky is blue.", "correct_answer": "True"},
    {"question": "2 + 2 = 5", "correct_answer": "False"},
    {"question": "Python is a species of snake.", "correct_answer": "True"},
    # Add more questions as needed
]
```

---

## 💡 Example Console Output

```
Q1: The sky is blue. (True/False)? true
You're right!

Q2: 2 + 2 = 5 (True/False)? false
You're right!

...

You've completed the quiz
Your final score was: 10/12
```

---

## 🛠 Requirements

This project uses only **standard Python libraries**. No external packages are required.

---

Enjoy the quiz!


