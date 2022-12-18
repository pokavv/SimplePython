import turtle

turtle_1 = turtle.Turtle()
screen = turtle.Screen()

def move_forwards():
    turtle_1.forward(10)

screen.listen()
screen.onkey(key='space', fun=move_forwards)
screen.exitonclick()