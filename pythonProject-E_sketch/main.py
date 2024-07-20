from turtle import Turtle,Screen
tim=Turtle()
screen=Screen()

screen.listen()
def move_forward():
    tim.forward(15)
def move_backward():
    tim.backward(15)
def move_clockwise():
    tim.right(15)
def move_anticlockwise():
    tim.left(15)
def clear_screen():
    tim.reset()
screen.onkey(key='w', fun=move_forward)
screen.onkey(key='s', fun=move_backward)
screen.onkey(key='a', fun=move_clockwise)
screen.onkey(key='d', fun=move_anticlockwise)
screen.onkey(key='c',fun=clear_screen)
screen.exitonclick()
