from turtle import Turtle, Screen
import random

# Create new Turtle
turtle_1 = Turtle()
turtle_1.shape('turtle')
turtle_1.pensize(15)
turtle_1.speed('fastest')

# color list
color_list = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

# set directions
directions = [0, 90, 180, 270]

# Draw random walk
for _ in range(100):
    turtle_1.color(random.choice(color_list))
    turtle_1.forward(30)
    turtle_1.setheading(random.choice(directions))

# Set Screen
screen = Screen()
screen.exitonclick()