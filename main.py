import turtle
from random import randint, randrange

screen = turtle.getscreen()
turtle = turtle.Turtle()

screen.bgcolor('black')
screen.colormode(255)


turtle.speed(100)
turtle.color('white')
turtle.penup()
turtle.shape('circle')
turtle.shapesize(0.05, 0.05)

P1 = (-200, -100)
P2 = (200, -100)
P3 = (0, 200)
last_point = (0, 100)
POINTS = [P1, P2, P3]

turtle.goto(P1)
turtle.dot(5)

turtle.goto(P2)
turtle.dot(5)

turtle.goto(P3)
turtle.dot(5)

turtle.goto(last_point)
turtle.stamp()

for i in range(0, 20000):
    random_point = POINTS[randint(0, 2)]
    
    mid_point = (
        (random_point[0] + last_point[0]) / 2,
        (random_point[1] + last_point[1]) / 2,
    )

    turtle.goto(mid_point)
    turtle.stamp()
    last_point = mid_point
    color = (randrange(0, 255), randrange(0, 255), randrange(0, 255))
    turtle.color(color)

screen.exitonclick()