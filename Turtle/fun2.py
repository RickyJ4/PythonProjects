from turtle import *
import colorsys

bgcolor("black")
tracer(100)

h = 0.7
c = colorsys.hsv_to_rgb(h,1,1)
pensize(4)

def draw():
    global h
    for i in range(4):
        c = colorsys.hsv_to_rgb(h,1,1)
        fillcolor(c)
        h+=0.004
        begin_fill()
        fd(50)
        right(20)
        fd(40)
        right(9)
        end_fill()

for i in range(400):
    draw()
    goto(0,0)
    rt(1)
done()
