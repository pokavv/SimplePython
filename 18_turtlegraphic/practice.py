from turtle import Turtle, Screen

# Creat Turtle object
turtle_1 = Turtle()

# Set Turtle appearence
turtle_1.shape('turtle')
turtle_1.color('green')

# Move Turtle
turtle_1.forward(150)

# Set Turtle direction
turtle_1.right(90)

# Set Screen
screen = Screen()
screen.exitonclick()