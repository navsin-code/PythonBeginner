# Typing Speed Test (GUI Version)

This is a Python-based GUI application that allows users to test their typing speed and accuracy. It uses the `tkinter` library for building the graphical user interface and calculates Words Per Minute (WPM) and typing accuracy based on a randomly selected sample text.

## Features

- 📝 Displays a random sample text for typing.
- ⏱️ Starts timing when the user begins typing.
- ✅ Calculates:
  - Words Per Minute (WPM)
  - Accuracy (percentage of correct characters)
- 🎨 Clean and aesthetic UI using `tkinter`.
- 🔁 Reset functionality to restart the test.

## Requirements

- Python 3.x
- No external libraries required (only uses Python’s built-in `tkinter`, `random`, and `time` modules)

## How to Run

1. Make sure Python is installed on your system.
2. Save the Python script to a file, for example: `typing_test.py`
3. Run the script:

```bash
python typing_test.py
````

## How It Works

1. Click the **Start Test** button.
2. A sample sentence will appear.
3. Type the sentence in the input box exactly as shown.
4. Once the text matches, the test ends automatically.
5. A pop-up message shows your WPM and accuracy.

## Code Overview

* `TypingSpeedTest` class manages the UI and typing logic.
* Sample sentences are stored in a list and chosen at random.
* Uses `Text` widgets for both displaying and typing text.
* Accuracy is computed by comparing character-by-character input with the original sentence.



