from turtle import Turtle, Screen

turtle_1 = Turtle()
turtle_1.shape('turtle')
turtle_1.color('green')

for _ in range(10):
    turtle_1.forward(10)
    turtle_1.penup()
    turtle_1.forward(10)
    turtle_1.pendown()

screen = Screen()
screen.exitonclick()