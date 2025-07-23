# German-English Flashcard App 

## Features ✨
- **Interactive Flashcards**: Presents German words and flips to show English translations after 3 seconds.
- **Progress Tracking**: Automatically removes known words and saves remaining ones in `Words_to_learn.csv`.
- **Randomized Practice**: Displays a random word each time for varied learning.
- **Error Handling**: Loads fallback data if saved progress file doesn't exist.

## Installation 🛠
1. Make sure Python 3.x is installed on your system.
2. Install dependencies:
   ```bash
   pip install pandas

3. Ensure the following folder structure exists:

   ```
   ├── images
   │   ├── card_front.png
   │   ├── card_back.png
   │   ├── right.png
   │   └── wrong.png
   ├── data
   │   ├── german_cards - Sheet1.csv
   │   └── Words_to_learn.csv (auto-created)
   └── main.py
   ```

## Usage 

1. Save the code in a file (e.g. `main.py`).
2. Run it with:

   ```bash
   python main.py
   ```
3. Click ❌ if you didn’t know the word, ✅ if you did. The app will flip cards and track known words.

## How It Works 🧩

* The app tries to load a saved learning progress file (`Words_to_learn.csv`). If it doesn’t exist, it loads from the original dataset `german_cards - Sheet1.csv`.
* It shows a German word on a flashcard, then flips to show the English version after a 3-second delay using `window.after`.
* When you click the ✅ button, the word is removed from the list and the updated list is saved.
* The interface is created using `tkinter` and images are used for the front/back of the card and buttons.
* Core functions:

  * `next_card()`: Loads a random word and sets a timer to flip.
  * `flip_card()`: Displays the English translation and updates the card image.
  * `is_known()`: Removes the known word, saves progress, and moves to the next card.

```

Let me know if you want to add links, screenshots, or a "Known Issues" section next!
```
