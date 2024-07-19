import time
from turtle import *
bgcolor("black")
hideturtle()
penup()
for p in [1,2,3]:
    goto(p * 30,30)
    dot(15 ,'green')

while True:
    for n in [0,30]:
        ricky = Turtle()
        ricky.goto(0,50)
        ricky.color("yellow")
        ricky.speed(11)
        ricky.hideturtle()
        ricky.left(150)
        ricky.begin_fill()
        ricky.circle(50,270 + n)
        ricky.left(90)
        ricky.forward(50)
        ricky.right(90)
        ricky.forward(50)
        ricky.end_fill()
        time.sleep(0.1)
        if n == 30:
            ricky.clear()
done()

screen = Screen()
screen.exitonclick