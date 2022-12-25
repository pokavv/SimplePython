from turtle import Turtle, Screen

turtle_1 = Turtle()
turtle_1.shape('turtle')
turtle_1.color('green')

def draw(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        turtle_1.forward(100)
        turtle_1.left(angle)

for side in range(3, 11):
    draw(side)

screen = Screen()
screen.exitonclick()