import turtle
from random import randint

screen = turtle.getscreen()
turtle = turtle.Turtle()

turtle.pen(pencolor='black', speed=12)
turtle.shapesize(0.05, 0.05)
turtle.penup()

P1 = (-200, -100)
P2 = (200, -100)
P3 = (0, 200)
last_point = (0, 150)

points = [P1, P2, P3]

turtle.goto(P1)
turtle.dot(8)

turtle.goto(P2)
turtle.dot(8)

turtle.goto(P3)
turtle.dot(8)

turtle.goto(last_point)
turtle.stamp()

for i in range(0, 20100):
    random_point = points[randint(0, 2)]
    mid_point = (
        (random_point[0] + last_point[0]) / 2,
        (random_point[1] + last_point[1]) / 2,
    )

    turtle.goto(mid_point)
    turtle.stamp()
    last_point = mid_point
