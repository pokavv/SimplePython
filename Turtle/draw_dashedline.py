from turtle import Turtle, Screen

# Create new Turtle
turtle_1 = Turtle()

# Turtle appearance
turtle_1.shape('turtle')
turtle_1.color('green')

# Draw Dashed Line
for _ in range(20):
    turtle_1.penup()
    turtle_1.forward(10)
    turtle_1.pendown()
    turtle_1.forward(10)

# Set Screen
screen = Screen()
screen.exitonclick()