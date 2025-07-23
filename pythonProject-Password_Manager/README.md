# Password Manager

This project is a **Password Manager GUI application** built with Python using the **Tkinter** library. It allows users to:
- Generate strong random passwords
- Save website login details (website, email, password) to a local JSON file
- Retrieve saved credentials using a built-in search
- Automatically copy generated passwords to clipboard for convenience

---

## Features

### 🔐 Password Generator
- Generates a strong, random password with:
  - Letters (uppercase & lowercase)
  - Numbers
  - Symbols
- Automatically copies the generated password to clipboard using `pyperclip`.

### 💾 Save Credentials
- Stores the website, email/username, and password securely in a local `password_manager.json` file.
- Uses `json` to store data in a structured, readable format.
- Updates existing data without overwriting the whole file.

### 🔍 Search Function
- Search by website name.
- If the credentials exist, displays email and password using a popup box.
- If not found, it shows a relevant error message.

### Data Validation & Error Handling
- Ensures fields are not empty before saving.
- Alerts user with meaningful messages if data is missing or file doesn't exist.

---

## How to Use

### Requirements
Ensure the following Python packages are installed:
- `tkinter` (standard with Python)
- `pyperclip` (`pip install pyperclip`)
- `json` and `random` are built-in

### ▶️ Running the App
1. Place your `logo.png` file in the same directory as this script.
2. Run the script:
   ```bash
   python password_manager.py
