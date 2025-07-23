# Hangman Game 🎯

## Features ✨
- **Word Guessing Logic**: Guess letters to reveal the hidden word one character at a time.
- **Life System**: You have 6 lives; each wrong guess costs one life.
- **ASCII Art Display**: Shows a hangman stage after each incorrect guess.
- **Duplicate Guess Warning**: Informs you if you guess the same correct letter again.

## Installation 🛠️
1. Ensure Python 3.x is installed.
2. Create a Python file (e.g. `hangman.py`) and make sure the following module files are in the same folder:
   - `hangman_words.py` — contains the list `word_list` with words to guess.
   - `art.py` — contains:
     - `logo`: the Hangman logo as a string.
     - `stages`: a list of strings for each visual stage of the hangman.

3. Example content for `hangman_words.py`:
   ```python
   word_list = ["python", "java", "kotlin", "hangman", "variable"]

4. Example content for `art.py`:

   ```python
   logo = "HANGMAN GAME"
   stages = ["stage 6", "stage 5", "stage 4", "stage 3", "stage 2", "stage 1", "stage 0"]
   ```

## Usage 🚀

1. Save the code in a file (e.g. `hangman.py`).
2. Run it using:

   ```bash
   python hangman.py
   ```
3. Enter a letter when prompted.
4. Keep guessing until you either guess all letters or run out of lives.

## How It Works 🧩

* The program selects a random word from `word_list` in `hangman_words.py`.
* A list of underscores (`_`) is displayed representing unguessed letters.
* The player types a letter:

  * If correct, the letter is revealed in all matching positions.
  * If incorrect, lives are reduced by 1 and a stage of the hangman is shown using `art.stages`.
  * If a correct letter is guessed again, a message is shown but no penalty is applied.
* The game ends when:

  * All letters are guessed → **You win**.
  * All lives are lost → **You lose**, and the correct word is revealed.

