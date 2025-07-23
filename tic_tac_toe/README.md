# ❌⭕ Tic Tac Toe (Console Version)

A simple two-player **Tic Tac Toe** game played in the terminal. The game logic uses a 3x3 board where players alternate turns, trying to get three marks in a row horizontally, vertically, or diagonally.

## 🧠 Concepts Demonstrated

- 2D list manipulation
- Input validation and exception handling
- Game logic and win condition checking
- Basic procedural programming

## ▶️ How to Play

1. Run the script:
   ```bash
   python tic_tac_toe.py
   
2. Players take turns entering their moves by specifying the **row** and **column** (both 0-indexed).

3. The board updates after each move. A player wins by placing three of their marks in a row, column, or diagonal.

4. If all cells are filled without a winner, the game ends in a tie.

## 🕹️ Controls

* Input format:

  ```bash
  Player X, enter row and column: 0 1
  ```

* Rows and columns must be integers from `0` to `2`.

## 🗂️ File Structure

```
tic_tac_toe/
└── tic_tac_toe.py   # Main game file
```

## 📌 Features

* 3x3 board printed after each move
* Win detection in all directions (rows, columns, diagonals)
* Input error handling (invalid numbers, occupied cells)
* Player switching and draw detection

---

### 🔧 Customization Ideas

* Add single-player mode with AI opponent
* Track and display scores over multiple rounds
* Add colored output using libraries like `colorama`
* Create a GUI version using Tkinter or Pygame


