
# 🐢 Turtle Racing Game

A simple arcade-style crossing game built using Python's `turtle` graphics module. The player controls a turtle that must cross a road while dodging moving cars. Each successful crossing increases the level and game difficulty.

## 🎮 Gameplay

- Use the **Up** and **Down** arrow keys to move the turtle.
- Dodge the oncoming cars.
- Each successful crossing increases the level and car speed.
- Game ends if the turtle collides with a car.

## 🧠 Concepts Demonstrated

- OOP (Object-Oriented Programming)
- Class inheritance and encapsulation
- Event-driven programming with `turtle.onkeypress`
- Simple game loop and collision detection

## 📁 Folder Structure

```

turtle\_crossing\_game/
├── main.py             # Main game loop
├── player.py           # Player (turtle) class
├── car\_manager.py      # Car generation and movement logic
├── scoreboard.py       # Level display and Game Over screen



## 🐍 Requirements

- Python 3.x
- No external libraries required — uses Python’s built-in `turtle` module

## ▶️ How to Run

1. Ensure all `.py` files (`main.py`, `player.py`, `car_manager.py`, `scoreboard.py`) are in the same folder.
2. Run the game:

```bash
python main.py
````

## 📌 Controls

| Key | Action           |
| --- | ---------------- |
| ↑   | Move turtle up   |
| ↓   | Move turtle down |

---

## 🔧 Customization Ideas

* Add lives instead of ending on first hit.
* Introduce score counting based on distance or time.
* Add background music or sound effects.
* Make cars spawn in different colors or patterns.


