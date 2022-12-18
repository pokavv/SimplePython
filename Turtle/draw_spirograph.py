from turtle import Turtle, Screen
import turtle as t
import random

turtle_1 = Turtle()
turtle_1.shape('turtle')
turtle_1.speed('fastest')

# color list: Use 'random', 'rgb(255)'
t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def draw_spirograph(gap_size):
    for _ in range(int(360 / gap_size)):
        turtle_1.color(random_color())
        turtle_1.circle(100)
        turtle_1.setheading(turtle_1.heading() + gap_size)

draw_spirograph(5)

screen = Screen()
screen.exitonclick()