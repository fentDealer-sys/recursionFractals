import tree
from turtle import *
from math import floor

speed(10)
tracer(9000)
hideturtle()
colormode(255)

a = 80
depth1 = 13
colorincrement = 255/depth1
width1 = depth1
widthincrement = width1/depth1

width(width1)

color(floor(0+colorincrement*depth1), floor(0+colorincrement*depth1), floor(0+colorincrement*depth1))

tree.canopy(5, depth1, a)

done()