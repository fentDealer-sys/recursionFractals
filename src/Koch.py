from turtle import *

speed("fastest")

def koch(a, order):
    if order > 0:
        for t in [60, -120, 60, 0]:
            koch(a/3, order-1)
            left(t)
    else:
        forward(a)

color("gold", "gold")
bgcolor("black")
size = 300
order = 9

penup()
backward(size/1.732)
left(30)
pendown()

tracer(10000)
hideturtle()

begin_fill()

for i in range(3):
    koch(size, order)
    right(120)

end_fill()
update()
exitonclick()