# import colorgram
# colours=colorgram.extract('painting1.jpeg',30)
# rgb_colours=[]
# for colour in colours:
#  r=colour.rgb.r
#  g=colour.rgb.g
#  b=colour.rgb.b
#  new_colour=(r,g,b)
#  rgb_colours.append(new_colour)
#
# print(rgb_colours)
from turtle import Turtle,Screen
import random
tim=Turtle()
colour_list=[(185, 162, 132), (129, 92, 70), (79, 93, 118), (147, 161, 180), (179, 152, 162), (210, 207, 135), (28, 35, 49), (119, 79, 92), (54, 24, 33), (46, 25, 19), (147, 170, 154), (86, 107, 91), (161, 156, 60), (113, 31, 43), (168, 107, 98), (27, 37, 33), (51, 58, 92), (212, 179, 189), (110, 123, 155), (117, 37, 27), (161, 107, 118), (219, 178, 170), (177, 202, 186), (180, 187, 209), (106, 144, 116), (67, 75, 35)]
tim.speed("fastest")
screen=Screen()
screen.colormode(255)
tim.setheading(225)
tim.penup()
tim.forward(300)
tim.setheading(0)
tim.pendown()
def dots():
    for i in range(10):
            tim.dot(20,random.choice(colour_list))
            tim.penup()
            tim.forward(50)
            tim.pendown()
for j in range(10):
    dots()
    tim.penup()
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)
    tim.pendown()


screen.exitonclick()