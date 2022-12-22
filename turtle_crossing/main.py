import time
from turtle import Turtle, Screen
from player import Player
from scoreboard import Scoreboard
from obstacle import Obstacle


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('white')
screen.title('turtle crossing')
screen.tracer(0)

player = Player()
obstacle = Obstacle()
score = Scoreboard()

screen.listen()
screen.onkey(player.go_up, 'Up')
screen.onkey(player.go_down, 'Down')

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    
    # create new obstacle
    obstacle.create_obs() 
    obstacle.move_obs()
    
    # detect collision with obstacle
    for obs in obstacle.all_obs:
        if obs.distance(player) < 20:
            game_on = False
            score.game_over()
    
    # detect crossing
    if player.is_finish_line():
        player.goto_start()
        obstacle.level()
        score.level_up()

screen.exitonclick()