# Turtle Etch-A-Sketch 🎨

## Features ✨
- **Keyboard-Controlled Drawing**: Use W, A, S, D keys to move the turtle and draw on the screen.
- **Reset Functionality**: Press `C` to clear the entire screen and reset the turtle position.
- **Interactive Canvas**: Draw in real-time using the built-in turtle graphics module.
- **Directional Movement**: Move forward/backward or rotate clockwise/anticlockwise.

## Installation 🛠️
1. Ensure Python 3.x is installed on your system.
2. No external libraries are needed — the script uses Python's built-in `turtle` module.

## Usage 🚀
1. Save the code in a file (e.g. `etch_a_sketch.py`).
2. Run it with:
   ```bash
   python etch_a_sketch.py

3. Controls:

   * `W` → Move forward
   * `S` → Move backward
   * `A` → Rotate right
   * `D` → Rotate left
   * `C` → Clear screen and reset turtle
   * Click on the screen to exit

## How It Works 🧩

* The script creates a `Turtle` object (`timmy`) and binds keyboard events using `onkey()` from the `Screen` object.
* Movement is handled by individual functions: `move_forward`, `move_backward`, `move_clockwise`, and `move_anticlockwise`.
* Pressing `C` triggers the `reset()` method, clearing the canvas and bringing the turtle to the center.
* The program continuously listens for keyboard events using `screen.listen()` and terminates when you click anywhere on the turtle screen (`screen.exitonclick()`).

```

