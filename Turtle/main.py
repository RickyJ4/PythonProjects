import turtle as t
import colorsys

t.Screen().bgcolor("black")
ricky = t.Turtle()
h = 0.3

def a_smart(len,ang=0,cl="#000000", c ="black"):
    ricky.seth(ang)
    ricky.fillcolor(cl)
    ricky.begin_fill()
    ricky.forward(len)
    ricky.seth(60+ang)
    ricky.forward((73/200)*len)
    ricky.seth(150+ang)
    ricky.forward((73/200)*len)
    ricky.seth(210+ang)
    ricky.forward(len)
    ricky.end_fill()

    ricky.fillcolor(c)
    ricky.begin_fill()
    ricky.seth(ang+0.01)
    ricky.forward(len/2)
    ricky.circle((13/200)*len,180)
    ricky.seth(30+ang)
    ricky.circle((13/200)*len,180)
    ricky.forward(len/2)
    ricky.end_fill()

for i in range(12):
    c = colorsys.hsv_to_rgb(h,1,1)
    cl = colorsys.hsv_to_rgb(h+0.5,1,1)
    ricky.pencolor(c)
    a_smart(280,i*30,c,cl)
    h += 0.15

ricky.ht()

t.done()

    





#screen = Screen()

#screen.exitonclick()

