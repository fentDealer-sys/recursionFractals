from turtle import *

bgcolor("slategray")
color("gold")

def arrowhead_curve(length, level, direction):
    if level == 0:
        forward(length)
    else:
        left(direction * 60)
        arrowhead_curve(length / 2, level-1, -direction)
        right(direction * 60)
        arrowhead_curve(length / 2, level - 1, direction)
        right(direction * 60)
        arrowhead_curve(length / 2, level - 1, -direction)
        left(direction * 60)

speed("fastest")
tracer(10000)
width(1.5)

penup()
goto(-400, -300)
pendown()

arrowhead_curve(800, 7, 1)
hideturtle()



update()
exitonclick()