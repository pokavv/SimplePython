from turtle import Turtle, Screen

turtle_1 = Turtle()
turtle_1.shape('turtle')
turtle_1.color('green')

for _ in range(4):
    turtle_1.forward(100)
    turtle_1.right(90)

screen = Screen()
screen.exitonclick()