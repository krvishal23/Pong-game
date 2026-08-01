from turtle import Screen, Turtle
from paddle import paddle
from ball import Ball
from scoreboard import scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong game")
screen.tracer(0)


r_paddle = paddle((350, 0))
l_paddle = paddle((-350, 0))
ball = Ball()
scoreboard = scoreboard()


screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")


game_is_on =True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()


    #detect collision with the paddles
    if ball.distance(r_paddle) < 40 and ball.xcor() > 300 or ball.distance(l_paddle) < 40 and ball.xcor() < -300:
        ball.bounce_x()

    if ball.xcor() > 380 :
        ball.reset_position()
        scoreboard.l_point()
    
    if ball.xcor() < -380 :
        ball.reset_position()
        scoreboard.r_point()



screen.exitonclick()