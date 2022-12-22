from turtle import Turtle
import random

COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
STARTING_MOVE = 5
INCREMENT = 10

class Obstacle(Turtle):
    
    def __init__(self):
        self.all_obs = []
        self.obs_speed = STARTING_MOVE
    
    def create_obs(self):
        random_create = random.randint(1, 10)
        if random_create == 1:
            new_obs = Turtle('square')
            new_obs.shapesize(stretch_wid=1, stretch_len=2)
            new_obs.penup()
            new_obs.color(random.choice(COLORS))
            
            random_y = random.randint(-250, 250)
            new_obs.goto(300, random_y)
            self.all_obs.append(new_obs)
    
    def move_obs(self):
        for obs in self.all_obs:
            obs.backward(STARTING_MOVE)
    
    def level(self):
        self.obs_speed += INCREMENT