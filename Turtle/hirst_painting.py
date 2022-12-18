'''
import colorgram

rgb = []
colors = colorgram.extract('c:/users/admin/desktop/project/simplepython/turtle/dot_image.jpg', 40)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_colors = (r, g, b)
    rgb.append(new_colors)

print(rgb)
'''

import turtle
import random

# create new Turtle
turtle_1 = turtle.Turtle()
turtle_1.speed('fastest')

# Hide line and turtle
turtle_1.penup()
turtle_1.hideturtle()

# Create color list
turtle.colormode(255)
color_list = [(18, 114, 167), (163, 80, 48), (208, 159, 92), (186, 13, 63), (131, 180, 201), (230, 78, 49), (36, 137, 84), (7, 35, 89), (148, 163, 37), (76, 41, 22), (166, 48, 91), (113, 186, 165), (223, 120, 149), (20, 169, 208), (62, 159, 92), (215, 72, 118), (8, 94, 52), (238, 163, 191), (95, 21, 68), (147, 205, 223), (213, 223, 9), (12, 87, 107), (247, 170, 146), (11, 46, 125), (160, 211, 188), (7, 75, 40), (163, 190, 225), (112, 44, 35), (108, 123, 161), (85, 
62, 37), (244, 13, 23)]

# initial position
turtle_1.setheading(225)
turtle_1.forward(300)
turtle_1.setheading(0)
dot_num = 100

# dot run
for dot in range(1, dot_num + 1):
    turtle_1.dot(20, random.choice(color_list))
    turtle_1.forward(50)

    if dot % 10 == 0:
        turtle_1.setheading(90)
        turtle_1.forward(50)
        turtle_1.setheading(180)
        turtle_1.forward(500)
        turtle_1.setheading(0)

# Set screen
screen = turtle.Screen()
screen.exitonclick()