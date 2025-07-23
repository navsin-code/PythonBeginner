# Kanye Says... 🗣️

## Features ✨
- **Live Quotes**: Fetches random Kanye West quotes from the `https://api.kanye.rest` API.
- **Interactive UI**: Click the Kanye button to generate a new quote.
- **Stylish Design**: Displays quotes over a themed background using `tkinter`.

## Installation 🛠️
1. Make sure Python 3.x is installed.
2. Install the required `requests` library:
   ```bash
   pip install requests

3. Ensure the following files are in the same directory:

   * `background.png` — background image for the canvas.
   * `kanye.png` — image used for the Kanye quote button.

## Usage 🚀

1. Save the code in a file (e.g. `kanye_quotes.py`).
2. Run the program:

   ```bash
   python kanye_quotes.py
   ```
3. Click on the Kanye button to fetch and display a new quote each time.

## How It Works 🧩

* The app uses Python’s `tkinter` to build a GUI with a background image and quote display.
* When the Kanye button is clicked, the `get_quote()` function sends a GET request to `https://api.kanye.rest`.
* The response is parsed from JSON, extracting the `"quote"` key.
* The quote is then displayed on the canvas by updating the `quote_text` item using `canvas.itemconfig`.
* The quote text is wrapped inside a width-limited text box for better readability on the background image.


