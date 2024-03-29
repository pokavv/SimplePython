from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]
    
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_body(position)
    
    def move(self):
        for num in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[num - 1].xcor()
            new_y = self.snake[num - 1].ycor()
            self.snake[num].goto(new_x, new_y)
        self.head.forward(MOVE)
    
    def add_body(self, position):
        body = Turtle('square')
        body.color('white')
        body.penup()
        body.goto(position)
        self.snake.append(body)
    
    def extend(self):
        self.add_body(self.snake[-1].position())
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    
    def reset(self):
        for s in self.snake:
            s.goto(1000, 1000)
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]