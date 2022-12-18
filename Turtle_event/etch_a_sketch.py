# w = foward, s = backward, a = counter-clockwise, d = clockwise, c = clear-drawing
# E = 0, N = 90, W=180, S = 270

import turtle

turtle_1 = turtle.Turtle()
screen = turtle.Screen()

# w = foward
def move_forwards():
    turtle_1.forward(10)

# s = backward
def move_backwards():
    turtle_1.back(10)

# a = counter-clockwise
def counter_clockwise():
    new_heading = turtle_1.heading() + 10
    turtle_1.setheading(new_heading)

# d = clockwise
def clockwise():
    new_heading = turtle_1.heading() - 10
    turtle_1.setheading(new_heading)

# c = clear-drawing
def clear_drawing():
    turtle_1.clear()
    turtle_1.penup()
    turtle_1.home()
    turtle_1.pendown()

# listen key event 
screen.listen()
screen.onkey(key='w', fun=move_forwards)
screen.onkey(key='s', fun=move_backwards)
screen.onkey(key='a', fun=counter_clockwise)
screen.onkey(key='d', fun=clockwise)
screen.onkey(key='c', fun=clear_drawing)
screen.exitonclick()