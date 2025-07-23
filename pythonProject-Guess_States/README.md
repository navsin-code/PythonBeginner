
# India States Guessing Game

## Features ✨
- **Interactive Quiz**: Users guess the names of Indian states by typing into input prompts.
- **Map-Based Learning**: Correct guesses are displayed directly on a map of India at their respective coordinates.
- **Progress Tracking**: Keeps track of how many states have been correctly guessed.
- **Exit Option**: Type `exit` anytime to quit the game early.

## Installation 🛠️
1. Ensure Python 3.x is installed on your system.
2. Install the required library:
   ```bash
   pip install pandas


3. Place the following files in the same directory as your script:

   * `indian map (1).gif` — map image file of India
   * `states coordinates - Sheet1.csv` — CSV file containing state names and their x, y coordinates

## Usage 🚀

1. Save the code in a file (e.g. `india_states_game.py`).
2. Make sure the image and CSV file are in the same folder.
3. Run the program:

   ```bash
   python india_states_game.py
   ```
4. A blank map of India will appear.
5. Type the name of a state in the prompt. If it's correct, the name will be displayed on the map at the appropriate location.
6. Type `exit` or close the input box to end the game.

## How It Works 🧩

* The map is displayed using `turtle` by registering a `.gif` image shape.
* The program loads state names and their coordinates from a CSV using `pandas`.
* It runs a loop where it prompts the user to guess a state name.
* If the guess is correct and hasn't been guessed already:

  * A turtle writes the state name at the specified x, y coordinate.
  * The state is added to the `guessed_states` list.
* The loop continues until all states are guessed or the user types `exit`.

