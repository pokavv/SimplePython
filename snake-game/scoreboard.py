import os
from turtle import Turtle

PATH = './snake-game/data.txt'
ALIGNMENT = 'center'
FONT = ('Courier', 11, 'normal')

class scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        with open(PATH, 'r') as data:
            self.highscore = int(data.read())
        self.penup()
        self.color('white')
        self.goto(0, 270)
        self.hideturtle()
        self.update()
    
    def update(self):
        self.clear()
        self.write(f'Score: {self.score} High score: {self.highscore}', align=ALIGNMENT, font=FONT)
    
    def get_score(self):
        self.score += 1
        self.update()
    
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open(PATH, 'w') as data:
                data.write(f'{self.highscore}')
        self.score = 0
        self.update()
    
    '''
    def game_over(self):
        self.goto(0, 0)
        self.write(f'GAME OVER', align=ALIGNMENT, font=FONT)
    '''