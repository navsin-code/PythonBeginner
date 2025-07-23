# Dot Painting with Turtle 🎨🐢

## Features ✨
- **Hirst-style Dot Painting**: Generates a grid of colourful dots inspired by artist Damien Hirst.
- **Randomized Colours**: Picks colours from a pre-generated palette extracted from an image using `colorgram`.
- **Custom Color Palette**: Uses a static RGB list to avoid needing `colorgram` at runtime.
- **Turtle Graphics**: Visually satisfying dot pattern using Python's built-in turtle module.

## Installation 🛠️
1. Make sure Python is installed (version 3.x).
2. Save the script as `dot_painting.py`.
3. Required modules:
   - Built-in: `turtle`, `random`
   - (Optional) To generate your own colour palette, install `colorgram.py`:
     ```bash
     pip install colorgram.py
     ```

## Usage 🚀
1. Simply run the script:
   ```bash
   python dot_painting.py


2. A window will pop up showing a 10x10 grid of coloured dots.
3. Click anywhere on the screen to close the turtle window.

## How It Works 🧩

* A list of RGB tuples (`colour_list`) defines the palette (pre-extracted using `colorgram`).
* The turtle starts from the bottom-left, moving right and placing 10 coloured dots with spacing.
* After one row, it moves up and draws the next row — forming a 10x10 grid.
* Each dot is `20px` wide and spaced `50px` apart horizontally and vertically.
* The screen's color mode is set to `255` to support RGB tuples.

> Bonus: You can uncomment the `colorgram` section to extract your own palette from any image.

