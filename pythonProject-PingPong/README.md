# 🏓 Ping-Pong Game

This is a classic **Ping-Pong game** (also known as **Pong**) built using Python's `turtle` module. The game is designed for **2 players**, where each player controls a paddle and competes to bounce the ball past their opponent to score points.

---

## 🎮 Gameplay

- The **left paddle** is controlled using:
  - `W` key to move **up**
  - `S` key to move **down**
- The **right paddle** is controlled using:
  - `Up Arrow` to move **up**
  - `Down Arrow` to move **down**

---

## 📁 Project Structure

```

ping\_pong\_game/
├── main.py             # Main game loop and screen setup
├── user\_paddle.py      # Paddle class definitions
├── ball.py             # Ball behavior (movement, bouncing)
├── scoreboard.py       # Score tracking and display
└── README.md           # This file

````

---

## 🛠 Requirements

- Python 3.x
- No external libraries are needed – only the built-in `turtle` and `time` modules.

---

## ▶️ How to Run

1. Make sure all the files (`main.py`, `user_paddle.py`, `ball.py`, `scoreboard.py`) are in the same folder.
2. Run the game:

```bash
python main.py
````

3. Use the controls and have fun!

---

## 📌 Features

* Real-time ball and paddle movement using `turtle` graphics.
* Dynamic difficulty using `move_speed` that resets after each point.
* Scoreboard display for each player.
* Ball bounces off walls and paddles.
* Ends only when you close the window.

---

## Learning Highlights

This project reinforces:

* OOP in Python
* Collision detection and event handling
* GUI handling with `turtle.Screen()`
* Animation via `screen.update()` and `time.sleep()`

---


