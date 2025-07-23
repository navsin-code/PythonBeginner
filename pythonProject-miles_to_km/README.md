# 📏 Miles to Kilometers Converter 

A simple GUI application built using Python's `tkinter` module. It converts distance from **miles** to **kilometers** and displays the result instantly upon button click.

---

## 💻 Features

- Simple and clean GUI layout
- Entry field for user input in miles
- Button to trigger conversion
- Output label showing the result in kilometers
- Uses accurate conversion factor: `1 mile = 1.609344 kilometers`

---

## 🧪 Example

```

\[Miles]        \[Convert Button]
↓                ↓
5.0       →     8.0467 Km


---

## 📋 Code Overview

```python
from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=200, height=200)

# Entry field for miles
input = Entry(width=10)
input.grid(column=1, row=0)

# Static labels
Label(text="Miles", font=("Arial", 15)).grid(column=2, row=0)
Label(text="is equal to", font=("Arial", 15)).grid(column=0, row=2)
Label(text="Km", font=("Arial", 15)).grid(column=2, row=2)

# Output label to display result
label4 = Label(text="0", font=("Arial", 15))
label4.grid(column=1, row=2)

# Conversion function
def output():
    miles = float(input.get())
    kilometer = round(miles * 1.609344, 4)
    label4.config(text=str(kilometer))

# Button to trigger conversion
Button(text="Click me", command=output).grid(column=1, row=3)

window.mainloop()
````

---

## ✅ Requirements

* Python 3.x
* No external dependencies (uses built-in `tkinter`)

---

## 🚀 How to Run

1. Save the script as `converter.py`
2. Run it via terminal or your Python IDE:

```bash
python converter.py
```

---

## 🎯 Output

* You input miles (e.g., `5`)
* Click the **"Click me"** button
* It outputs kilometers (`8.0467`) rounded to 4 decimal places

---

## 🧠 Concepts Used

* GUI programming using `tkinter`
* Grid layout system
* Event-driven callback (`command=output`)
* String-to-float conversion and label update

---


