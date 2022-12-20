from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 11, 'normal')

class scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color('white')
        self.goto(0, 270)
        self.hideturtle()
        self.update()
    
    def update(self):
        self.write(f'Score: {self.score}', align=ALIGNMENT, font=FONT)
    
    def get_score(self):
        self.score += 1
        self.clear()
        self.update()
    
    def game_over(self):
        self.goto(0, 0)
        self.write(f'GAME OVER', align=ALIGNMENT, font=FONT)