import os
from turtle import *
from savefile import png
import ghostscript

speed("fastest")
tracer(5000)
hideturtle()
bgcolor("black")
color("lime")
hideturtle()
lt(90)

def fern(depth, a, alpha):
    # hedgehog.lt(90)
    if depth==0:
        return
    color("green")
    pensize(depth)
    fd(a/3)
    rt(60)
    fern(depth-1, 2*a/5, alpha)
    lt(60)
    pensize(depth)
    fd(a/2)
    lt(60)
    fern(depth - 1, 2*a/5, -alpha)
    rt(60)
    # hedgehog.fd(a / 6)
    # hedgehog.rt(60)
    # fern(hedgehog, depth - 1, a / 3, alpha)
    # hedgehog.lt(60)
    # hedgehog.fd(a/4)
    # hedgehog.lt(60)
    # fern(hedgehog, depth - 1, a / 3, -alpha)
    # hedgehog.rt(60)
    lt(alpha)
    fern(depth - 1, (a*4)/5, alpha)
    rt(alpha)
    bk(5*a/6)

penup()
goto(0, -250)
pendown()
fern(7, 100, 6)

update()

getscreen().getcanvas().postscript(file='outfile.ps')
png('outfile.ps')
os.remove('outfile.ps')
exitonclick()


