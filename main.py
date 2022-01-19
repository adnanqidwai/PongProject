from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.title("PONG")
screen.setup(width=800, height=600)
screen.tracer(0)

paddle_l = Paddle((-350, 0))
paddle_r = Paddle((350, 0))
game_is_on = True
score=Scoreboard()
ball = Ball()
screen.listen()
screen.onkey(paddle_r.up, "Up")
screen.onkey(paddle_r.down, "Down")
screen.onkey(paddle_l.up, "w")
screen.onkey(paddle_l.down, "s")
k=0
while game_is_on:
    time.sleep(ball.ballspeed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wallbounce()
    if (ball.xcor() > 320 and ball.distance(paddle_r) < 60) or (ball.xcor() < -320 and ball.distance(paddle_l) < 60):
        ball.paddlebounce()
        k+= 0.005
    if ball.xcor() > 350:
        # paddle r has missed
        ball.resetposition()
        score.lpoint()
        k=0
    if ball.xcor() < -350:
        # paddle r has missed
        ball.resetposition()
        score.rpoint()
        k=0

screen.exitonclick()
