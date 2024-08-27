from turtle import Turtle
class R_paddle(Turtle):
    def __init__(self):
        super().__init__()
        # self.hideturtle()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.goto(350,0)
        # self.showturtle()
    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
    def down(self):
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)

class L_paddle(Turtle):
        def __init__(self):
            super().__init__()
            # self.hideturtle()
            self.color("white")
            self.shape("square")
            self.shapesize(stretch_wid=5, stretch_len=1)
            self.penup()
            self.goto(-350,0)

        def w_key(self):
          new_y = self.ycor() + 20
          self.goto(self.xcor(), new_y)
        def s_key(self):
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)
