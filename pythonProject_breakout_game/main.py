import tkinter as tk
from tkinter import messagebox
import random

class BreakoutGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Breakout Game")
        self.root.geometry("600x600")
        self.root.configure(bg="#2C3E50")  # Dark blue-gray background

        # Game variables
        self.canvas_width = 600
        self.canvas_height = 600
        self.paddle_width = 80
        self.paddle_height = 10
        self.ball_size = 15
        self.brick_rows = 5
        self.brick_cols = 8
        self.brick_width = 60
        self.brick_height = 20
        self.brick_spacing = 10
        self.score = 0
        self.game_running = True
        self.paddle_speed = 10  # Pixels per key press
        self.paddle_dx = 0  # Paddle movement direction

        # Colors
        self.colors = ["#E74C3C", "#3498DB", "#F1C40F", "#2ECC71", "#9B59B6"]  # Red, Blue, Yellow, Green, Purple
        self.paddle_color = "#ECF0F1"  # Light gray
        self.ball_color = "#E67E22"  # Orange
        self.bg_color = "#34495E"  # Darker blue-gray for canvas

        # Canvas
        self.canvas = tk.Canvas(
            root,
            width=self.canvas_width,
            height=self.canvas_height,
            bg=self.bg_color,
            highlightthickness=0
        )
        self.canvas.pack(pady=10)

        # Score display
        self.score_label = tk.Label(
            root,
            text=f"Score: {self.score}",
            font=("Arial", 14, "bold"),
            fg="#ECF0F1",
            bg="#2C3E50"
        )
        self.score_label.pack(pady=5)

        # Paddle
        self.paddle = self.canvas.create_rectangle(
            self.canvas_width // 2 - self.paddle_width // 2,
            self.canvas_height - 40,
            self.canvas_width // 2 + self.paddle_width // 2,
            self.canvas_height - 40 + self.paddle_height,
            fill=self.paddle_color,
            outline=self.paddle_color
        )

        # Ball
        self.ball = self.canvas.create_oval(
            self.canvas_width // 2 - self.ball_size // 2,
            self.canvas_height // 2 - self.ball_size // 2,
            self.canvas_width // 2 + self.ball_size // 2,
            self.canvas_height // 2 + self.ball_size // 2,
            fill=self.ball_color,
            outline=self.ball_color
        )

        # Ball movement
        self.ball_dx = 5
        self.ball_dy = -5

        # Bricks
        self.bricks = []
        for row in range(self.brick_rows):
            for col in range(self.brick_cols):
                x1 = col * (self.brick_width + self.brick_spacing) + self.brick_spacing
                y1 = row * (self.brick_height + self.brick_spacing) + 50
                x2 = x1 + self.brick_width
                y2 = y1 + self.brick_height
                color = random.choice(self.colors)
                brick = self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline=color)
                self.bricks.append(brick)

        # Bind arrow keys
        self.canvas.bind("<Left>", self.start_move_left)
        self.canvas.bind("<Right>", self.start_move_right)
        self.canvas.bind("<KeyRelease-Left>", self.stop_move)
        self.canvas.bind("<KeyRelease-Right>", self.stop_move)
        self.canvas.focus_set()

        # Start game loop
        self.update_game()

    def start_move_left(self, event):
        self.paddle_dx = -self.paddle_speed

    def start_move_right(self, event):
        self.paddle_dx = self.paddle_speed

    def stop_move(self, event):
        self.paddle_dx = 0

    def move_paddle(self):
        # Get current paddle position
        paddle_pos = self.canvas.coords(self.paddle)
        new_x1 = paddle_pos[0] + self.paddle_dx
        new_x2 = paddle_pos[2] + self.paddle_dx

        # Keep paddle within canvas bounds
        if new_x1 < 0:
            new_x1 = 0
            new_x2 = self.paddle_width
        if new_x2 > self.canvas_width:
            new_x1 = self.canvas_width - self.paddle_width
            new_x2 = self.canvas_width

        self.canvas.coords(
            self.paddle,
            new_x1,
            self.canvas_height - 40,
            new_x2,
            self.canvas_height - 40 + self.paddle_height
        )

    def update_game(self):
        if not self.game_running:
            return

        # Move paddle
        self.move_paddle()

        # Move ball
        self.canvas.move(self.ball, self.ball_dx, self.ball_dy)
        ball_pos = self.canvas.coords(self.ball)

        # Wall collisions
        if ball_pos[0] <= 0 or ball_pos[2] >= self.canvas_width:
            self.ball_dx = -self.ball_dx
        if ball_pos[1] <= 0:
            self.ball_dy = -self.ball_dy
        if ball_pos[3] >= self.canvas_height:
            # Ball missed paddle
            self.game_running = False
            messagebox.showinfo("Game Over", f"Game Over! Score: {self.score}", parent=self.root)
            self.root.quit()
            return

        # Paddle collision
        paddle_pos = self.canvas.coords(self.paddle)
        if (ball_pos[3] >= paddle_pos[1] and ball_pos[1] <= paddle_pos[3] and
            ball_pos[0] >= paddle_pos[0] and ball_pos[2] <= paddle_pos[2]):
            self.ball_dy = -self.ball_dy

        # Brick collisions
        for brick in self.bricks[:]:
            brick_pos = self.canvas.coords(brick)
            if (ball_pos[3] >= brick_pos[1] and ball_pos[1] <= brick_pos[3] and
                ball_pos[0] >= brick_pos[0] and ball_pos[2] <= brick_pos[2]):
                self.canvas.delete(brick)
                self.bricks.remove(brick)
                self.ball_dy = -self.ball_dy
                self.score += 10
                self.score_label.config(text=f"Score: {self.score}")
                break

        # Check win condition
        if not self.bricks:
            self.game_running = False
            messagebox.showinfo("Victory!", f"You Win! Score: {self.score}", parent=self.root)
            self.root.quit()
            return

        # Continue game loop
        self.root.after(20, self.update_game)

if __name__ == "__main__":
    root = tk.Tk()
    game = BreakoutGame(root)
    root.mainloop()