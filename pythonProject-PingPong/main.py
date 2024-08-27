from turtle import Turtle,Screen
from user_paddle import R_paddle,L_paddle
from ball import Ball
from scoreboard import Score
import time
screen=Screen()
screen.listen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Ping-Pong Game")
screen.tracer(0)

r_paddle=R_paddle()
l_paddle=L_paddle()
ball=Ball()
score=Score()

screen.onkeypress(l_paddle.w_key,"w")
screen.onkeypress(l_paddle.s_key,"s")
screen.onkeypress(r_paddle.up,"Up")
screen.onkeypress(r_paddle.down,"Down")
game_is_on=True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()
    if ball.distance(r_paddle)<50 and ball.xcor()>320:
        ball.bounce_x()
    if ball.distance(l_paddle)<50 and ball.xcor()<-320:
        ball.bounce_x()
    if ball.xcor()>400:
        ball.goto(0,0)
        ball.move_speed = 0.1
        ball.bounce_x()
        score.r_scored()
    if ball.xcor() < -400:
        ball.goto(0, 0)
        ball.move_speed = 0.1
        ball.bounce_x()
        score.l_scored()






screen.exitonclick()