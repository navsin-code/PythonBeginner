import tkinter as tk
from tkinter import messagebox, font
import time
import random


class TypingSpeedTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        self.root.geometry("700x500")
        self.root.configure(bg="#2C3E50")  # Dark blue-gray background


        self.title_font = font.Font(family="Helvetica", size=16, weight="bold")
        self.text_font = font.Font(family="Courier New", size=12)
        self.button_font = font.Font(family="Arial", size=12, weight="bold")
        self.result_font = font.Font(family="Arial", size=14)


        self.sample_texts = [
            "The quick brown fox jumps over the lazy dog.",
            "Typing is a skill that improves with practice.",
            "Python is a versatile programming language.",
            "The sun sets slowly behind the mountain.",
            "A journey of a thousand miles begins with a single step."
        ]

        self.current_text = ""
        self.start_time = None
        self.test_running = False


        self.label_title = tk.Label(
            root,
            text="Typing Speed Test",
            font=self.title_font,
            fg="#ECF0F1",  # Light gray text
            bg="#2C3E50"
        )
        self.label_title.pack(pady=20)


        self.label_instruction = tk.Label(
            root,
            text="Type the text below after clicking Start",
            font=self.result_font,
            fg="#BDC3C7",  # Grayish text
            bg="#2C3E50"
        )
        self.label_instruction.pack(pady=5)


        self.text_display = tk.Text(
            root,
            height=3,
            width=50,
            font=self.text_font,
            bg="#ECF0F1",  # Light background
            fg="#2C3E50",  # Dark text
            wrap="word",
            borderwidth=2,
            relief="groove"
        )
        self.text_display.pack(pady=10)
        self.text_display.config(state="disabled")


        self.entry = tk.Text(
            root,
            height=3,
            width=50,
            font=self.text_font,
            bg="#FFFFFF",  # White background
            fg="#2C3E50",
            wrap="word",
            borderwidth=2,
            relief="groove"
        )
        self.entry.pack(pady=10)
        self.entry.config(state="disabled")


        self.button_frame = tk.Frame(root, bg="#2C3E50")
        self.button_frame.pack(pady=10)

        self.start_button = tk.Button(
            self.button_frame,
            text="Start Test",
            command=self.start_test,
            font=self.button_font,
            bg="#3498DB",  # Blue button
            fg="#FFFFFF",
            activebackground="#2980B9",
            borderwidth=2,
            relief="flat",
            width=12
        )
        self.start_button.pack(side=tk.LEFT, padx=10)

        self.reset_button = tk.Button(
            self.button_frame,
            text="Reset",
            command=self.reset_test,
            font=self.button_font,
            bg="#E74C3C",  # Red button
            fg="#FFFFFF",
            activebackground="#C0392B",
            borderwidth=2,
            relief="flat",
            width=12
        )
        self.reset_button.pack(side=tk.LEFT, padx=10)


        self.result_label = tk.Label(
            root,
            text="",
            font=self.result_font,
            fg="#F1C40F",  # Yellow text
            bg="#2C3E50"
        )
        self.result_label.pack(pady=20)

        
        self.reset_test()

    def start_test(self):
        if not self.test_running:
            self.test_running = True
            self.start_button.config(state="disabled", bg="#7F8C8D")  # Gray out when disabled
            self.entry.config(state="normal")
            self.entry.delete("1.0", tk.END)
            self.entry.focus()
            self.start_time = time.time()
            self.entry.bind("<KeyRelease>", self.check_typing)

    def check_typing(self, event=None):
        if self.test_running:
            typed_text = self.entry.get("1.0", tk.END).strip()
            if typed_text == self.current_text:
                self.test_running = False
                end_time = time.time()
                time_taken = end_time - self.start_time
                words = len(self.current_text.split())
                wpm = (words / time_taken) * 60
                accuracy = self.calculate_accuracy(typed_text, self.current_text)
                self.result_label.config(text=f"WPM: {wpm:.2f} | Accuracy: {accuracy:.2f}%")
                self.entry.config(state="disabled")
                self.start_button.config(state="normal", bg="#3498DB")  # Restore blue color
                messagebox.showinfo(
                    "Test Complete",
                    f"Your typing speed: {wpm:.2f} WPM\nAccuracy: {accuracy:.2f}%",
                    parent=self.root
                )

    def calculate_accuracy(self, typed, original):
        correct_chars = sum(1 for t, o in zip(typed, original) if t == o)
        total_chars = max(len(original), len(typed))
        return (correct_chars / total_chars) * 100 if total_chars > 0 else 0

    def reset_test(self):
        self.test_running = False
        self.current_text = random.choice(self.sample_texts)
        self.text_display.config(state="normal")
        self.text_display.delete("1.0", tk.END)
        self.text_display.insert(tk.END, self.current_text)
        self.text_display.config(state="disabled")
        self.entry.config(state="disabled")
        self.entry.delete("1.0", tk.END)
        self.result_label.config(text="")
        self.start_button.config(state="normal", bg="#3498DB")  # Restore blue color
        self.entry.unbind("<KeyRelease>")


if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTest(root)
    root.mainloop()