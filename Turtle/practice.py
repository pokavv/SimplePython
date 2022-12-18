from turtle import Turtle, Screen

# Create new Turtle
turtle_1 = Turtle()

# Turtle appearance
turtle_1.shape('turtle')
turtle_1.color('green')

# Move Turtle
turtle_1.forward(100)
turtle_1.left(90)

# Set Screen
screen = Screen()
screen.exitonclick()