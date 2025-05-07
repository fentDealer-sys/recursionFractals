from turtle import *
from imageGrab import capture_window

def sierpinski(a, level):
    if level == 1:
        for _ in range(0,3):
            fd(a)
            left(120)
    else:
        for _ in range(0,3):
            begin_fill()
            sierpinski(a/2, level-1)
            end_fill()
            fd(a)
            left(120)


width(2)
color("gold")
#fillcolor("gold")
bgcolor("slategray")

speed(0)
tracer(100)
hideturtle()
penup()
goto(-200, -100)
pendown()

begin_fill()
sierpinski(400, 7)
end_fill()

update()

capture_window()


done()

