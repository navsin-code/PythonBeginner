# Automated Letter Generator

## Features
- **Template-Based Letters**: Uses a single starter letter with a `[name]` placeholder to personalize content.
- **Batch Processing**: Automatically generates letters for all names listed in a text file.
- **File Output**: Saves each letter as a separate `.txt` file in the `ReadyToSend` directory.
- **Whitespace Handling**: Removes any trailing or leading spaces from names to ensure clean formatting.

## Installation
1. Make sure **Python 3.x** is installed on your machine.
2. Clone or download this repository.
3. No external libraries are required.

## Usage
1. Prepare your input files:
   - `./Input/Names/invited_names.txt` should contain one name per line.
   - `./Input/Letters/starting_letter.txt` should contain your template letter with the placeholder `[name]`.

2. Save the following script in a file, e.g. `main.py`:

   ```python
   PLACEHOLDER = '[name]'

   with open("./Input/Names/invited_names.txt") as names_file:
       names = names_file.readlines()

   with open("./Input/Letters/starting_letter.txt") as letter_file:
       letter_contents = letter_file.read()
       for name in names:
           stripped_name = name.strip()
           new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
           with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode='w') as final_letter:
               final_letter.write(new_letter)
