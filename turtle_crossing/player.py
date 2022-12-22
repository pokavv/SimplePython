from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_UP = 10
MOVE_DOWN = -10
FINISH_LINE = 280

class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.goto_start()
        self.setheading(90)
    
    def go_up(self):
        self.forward(MOVE_UP)
    
    def go_down(self):
        self.forward(MOVE_DOWN)
    
    def goto_start(self):
        self.goto(STARTING_POSITION)
    
    def is_finish_line(self):
        if self.ycor() > FINISH_LINE:
            return True
        else:
            return False