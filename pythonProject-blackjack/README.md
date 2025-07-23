# ♠️ Blackjack Game 

A simple console-based Blackjack game implemented in Python. This project demonstrates the use of functions, loops, conditionals, and randomization to simulate a playable version of the popular card game.

---

## 📁 Project Structure

```

blackjack/
├── blackjack.py       # Main script for the Blackjack game
├── art.py             # Contains ASCII logo used in the game
└── README.md          # Project documentation

````

---

## 🎮 Gameplay Features

- Player and computer are each dealt two cards initially.
- The game follows standard Blackjack rules:
  - A score of **21 with two cards** is a **Blackjack** (score = 0).
  - Aces (11) can be converted to 1 if the total score exceeds 21.
  - Player can choose to draw more cards or pass.
  - Computer draws cards until score reaches at least 17.
- Outcome is decided based on comparison of scores:
  - Win, Lose, Draw, Blackjack, or Bust.

---

## ▶️ How to Run

1. Make sure Python 3 is installed on your system.
2. Install required dependencies (if not already present):

```bash
pip install art
````

3. Place the following two files in the same directory:

   * `blackjack.py` (main script)
   * `art.py` (containing the `logo` ASCII art)

4. Run the game:

```bash
python blackjack.py
```

---

## 🧠 Key Python Concepts Used

* Functions and function parameters
* Random number generation
* Conditional logic (`if`/`else`)
* Lists and list operations
* Loops (`while` and `for`)
* Simple use of external modules (`art`)
* Clean console experience using `os.system('clear')` or `cls`

---

## ✅ Requirements

* Python 3.x
* [art](https://pypi.org/project/art/) module for the game logo (ASCII text art)

Install via pip:

```bash
pip install art
```

---


