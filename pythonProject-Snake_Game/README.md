# 🐍 Snake Game (Python Turtle)

A classic Snake game built using Python's `turtle` module. Eat the food, grow longer, and avoid crashing into walls or yourself!

---

## 📁 Project Structure

```

snake\_game/
├── main.py           # Main game loop
├── snake.py          # Snake class (movement, growth, reset)
├── food.py           # Food class (random spawn)
├── scoreboard.py     # Scoreboard class (display, reset)
└── README.md         # This file

````

---

## ▶️ How to Run

1. Make sure Python 3.x is installed.
2. Place all the files in the same folder.
3. Run the game:

```bash
python main.py
````

---

## 🎮 Controls

* Arrow Keys:

  * `↑` → Move Up
  * `↓` → Move Down
  * `←` → Move Left
  * `→` → Move Right

---

## 🧠 Game Features

* Smooth snake movement using `turtle` animation
* Randomly spawning food
* Collision detection:

  * With food → Snake grows, score increases
  * With wall or self → Game resets, score resets
* Persistent scoreboard on screen
* Modular code structure using OOP (`Snake`, `Food`, `Scoreboard`)

---

## ✅ Requirements

* Python standard library only
* Uses:

  * `turtle`
  * `time`
  * `random`

No external dependencies needed.

---

Enjoy the game and try to beat your high score! 🎉


