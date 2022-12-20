from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

snake = Snake()
score = scoreboard()
food = Food()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    # Detect collision food
    if snake.head.distance(food) < 15:
        food.new_food()
        snake.extend()
        score.get_score()
    
    # Detect collision with wall
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        game_on = False
        score.game_over()
    
    '''
    # Detect collision with tail
    for body in snake.snake:
        if body == snake.head:
            pass
        elif snake.head.distance(body) < 10:
            game_on = False
            score.game_over()
    '''
    
    # slicing 이용해서 'Detect collision with tail' code 간소화
    for body in snake.snake[1:]:
        if snake.head.distance(body) < 10:
            game_on = False
            score.game_over()
    
screen.exitonclick()