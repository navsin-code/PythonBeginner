
# ⏳ Pomodoro Timer (Tkinter GUI)

This is a **Pomodoro Timer** app built using Python's `tkinter` GUI module. It follows the Pomodoro technique for time management: **25 minutes of work** followed by **short breaks**, with a **long break after 4 sessions**.

---

## 🧠 Pomodoro Technique Basics

- ✅ **Work session:** 25 minutes
- ☕ **Short break:** 5 minutes
- 😴 **Long break:** 20 minutes (after 4 work sessions)

---

## 📁 Project Structure

```

pomodoro\_timer/
├── main.py           # Complete Pomodoro timer logic and GUI
├── tomato.png        # Tomato image used in the timer GUI
└── README.md         # This file

````

---

## ▶️ How to Run

1. Make sure you have Python 3.x installed.
2. Place `main.py` and `tomato.png` in the same folder.
3. Run the Python script:

```bash
python main.py
````

> 🖼 Make sure `tomato.png` exists in the same directory – it's used as a background image for the timer.

---

## 🎮 Features

* GUI built with `tkinter`
* Dynamic timer with **countdown logic**
* Labels show whether it's **Work**, **Short Break**, or **Long Break**
* **Start** and **Reset** buttons
* Progress is marked with ✅ symbols

---

## 🔧 Controls

| Button | Action                              |
| ------ | ----------------------------------- |
| Start  | Begins the Pomodoro cycle           |
| Reset  | Stops and resets the timer to 00:00 |

---

## 🛠 Requirements

* Python 3.x
* Standard libraries only:

  * `tkinter`
  * `math`

---

## 📌 Learning Highlights

* Building interactive GUIs using `tkinter`
* Event-driven programming (`after()`, `after_cancel()`)
* Dynamic label updates and canvas manipulation
* Modular timer logic with session tracking

---

