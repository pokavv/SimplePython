# tuple: immutable, list: mutable

from turtle import Turtle, Screen
import turtle as t
import random

# Create new Turtle
turtle_1 = Turtle()
turtle_1.shape('turtle')
turtle_1.pensize(15)
turtle_1.speed('fastest')

# color list: Use 'random', 'rgb(255)'
t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

# set directions
directions = [0, 90, 180, 270]

# Draw random walk
for _ in range(100):
    turtle_1.color(random_color())
    turtle_1.forward(30)
    turtle_1.setheading(random.choice(directions))

# Set Screen
screen = Screen()
screen.exitonclick()