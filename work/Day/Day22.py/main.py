from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

tim = Turtle()

# ball = Ball(0,0)
screen=Screen()
screen.title("PingPong Game")
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.tracer(0)

# paddle = Paddle()
r_paddle=Paddle((350, 0))
l_paddle=Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")


game_is_on=True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detects collision with the wall.
    if ball.ycor()> 280 or ball.ycor()< -280:
        ball.bounce_y()

    #detects collision with the paddle.
    if ball.distance(r_paddle)<50 and ball.xcor()>340  or  ball.distance(l_paddle)<50 and ball.xcor()> -340:
        ball.bounce_x()


    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()