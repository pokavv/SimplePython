from turtle import Turtle, Screen
import random

# Create new Turtle
turtle_1 = Turtle()

# Turtle appearance
turtle_1.shape('turtle')
turtle_1.color('green')

# color list
color_list = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

# Draw various shape
def draw(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        turtle_1.forward(100)
        turtle_1.left(angle)

for side in range(3, 11):
    turtle_1.color(random.choice(color_list))
    draw(side)

# Set Screen
screen = Screen()
screen.exitonclick()