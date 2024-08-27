import turtle
from turtle import Turtle,Screen
import random
is_race_on=False
screen=Screen()
screen.setup(width=500,height=400)
user_bet=screen.textinput(title="Make your bet(V,I,B,G,Y,O,R)",prompt="Which turtle wins the race?Enter colour:")
colours=['violet','indigo','blue','green','yellow','orange','red']
y_positions=[-70,-40,-10,20,50,80,110]
all_turtles=[]
for turtle_index in range (7):
     new_turtle=Turtle(shape="turtle")
     new_turtle.color(colours[turtle_index])
     new_turtle.penup()
     new_turtle.goto(x=-230,y=y_positions[turtle_index])
     all_turtles.append(new_turtle)
if user_bet:
    is_race_on=True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_race_on=False
            winning_colour=turtle.pencolor()
            if winning_colour==user_bet:
                print(f"You Won,the {winning_colour} turtle is the winner")
            else:
                print(f"You Lost,the {winning_colour} turtle is the winner")
        distance=random.randint(0,11)
        turtle.forward(distance)
screen.exitonclick()