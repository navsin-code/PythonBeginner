from turtle import Turtle,Screen
timmy=Turtle()
screen=Screen()

screen.listen()
def move_forward():
    timmy.forward(15)
def move_backward():
    timmy.backward(15)
def move_clockwise():
    timmy.right(15)
def move_anticlockwise():
    timmy.left(15)
def clear_screen():
    timmy.reset()
screen.onkey(key='w', fun=move_forward)
screen.onkey(key='s', fun=move_backward)
screen.onkey(key='a', fun=move_clockwise)
screen.onkey(key='d', fun=move_anticlockwise)
screen.onkey(key='c',fun=clear_screen)
screen.exitonclick()
