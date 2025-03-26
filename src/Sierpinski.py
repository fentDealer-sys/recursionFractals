from turtle import *

width(1.5)
color("gold")
#fillcolor("gold")
bgcolor("slategray")

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


speed(0)
tracer(100)
hideturtle()
penup()
goto(-400, 0)
pendown()

begin_fill()
sierpinski(400, 9)
end_fill()

update()
exitonclick()