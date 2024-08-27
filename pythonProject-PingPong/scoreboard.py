from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score =0
        self.r_score=0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(-100,200)
        self.l_update_score()
        self.goto(100,200)
        self.r_update_score()
    def r_update_score(self):
            self.write(self.r_score, align="center", font=("Arial", 24, "normal"))
    def l_update_score(self):
        self.write(self.l_score, align="center", font=("Arial", 24, "normal"))
    def r_scored(self):
        self.r_score+=1
        self.clear()
        self.goto(-100, 200)
        self.r_update_score()
        self.goto(100, 200)
        self.l_update_score()
    def l_scored(self):
        self.l_score+=1
        self.clear()
        self.goto(-100, 200)
        self.r_update_score()
        self.goto(100, 200)
        self.l_update_score()
