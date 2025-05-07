from turtle import *
from math import radians, floor

speed(10)
tracer(9000)
hideturtle()
colormode(255)

a = 80
depth1 = 13
colorincrement = 255/depth1
widthturtle = depth1
widthincrement = widthturtle/depth1

width(widthturtle)

color(floor(0+colorincrement*depth1), floor(0+colorincrement*depth1), floor(0+colorincrement*depth1))

def canopy(angle, depth, length):
    if depth == 1:
        return
    if depth == depth1:
        setheading(90)
        forward((5 / 4) * a)
    startpos = pos()
    startheading = heading()
    color(floor(0+colorincrement*depth), floor(0+colorincrement*depth), floor(0+colorincrement*depth))
    width(depth-1)
    lt(angle)
    forward(length)
    canopy(angle, depth-1, length*0.75)
    penup()
    goto(startpos)
    pendown()
    setheading(startheading)
    color(floor(0+colorincrement*depth), floor(0+colorincrement*depth), floor(0+colorincrement*depth))
    width(depth-1)
    rt(angle)
    forward(length)
    canopy(angle, depth-1, length*0.75)

if __name__ == "__main__":
    teleport(0, -2.5*a)
    bgcolor("slategray")
    canopy(30, depth1, a)
    update()
    exitonclick()