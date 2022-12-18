from turtle import Turtle, Screen
import random

# initial setting
screen = Screen()
screen.setup(width=500, height=400)
race_on = False
player_list = []

# Set betting question
user_bet = screen.textinput(title='Bet your turtle', prompt='Which turtle will win the race? Bet a color: ')
print(user_bet)

# turtle color list
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

# turtle's starting y position list 
y_position = [-70, -40, -10, 20, 50, 80]

# Creating turtle objects through for loop
for t in range(0, 6):
    turtle_player = Turtle(shape='turtle')
    turtle_player.color(colors[t])
    turtle_player.penup()
    turtle_player.goto(x=-230, y=y_position[t])
    player_list.append(turtle_player)

# play turtle racing
if user_bet:
    race_on = True

while race_on:
    for t in player_list:
        if t.xcor() > 230:
            race_on = False
            win_turtle = t.pencolor()
            if win_turtle == user_bet:
                print(f'You win! The {win_turtle} turtle is the winner!')
            else:
                print(f'You lose.. The {win_turtle} turtle is the winner..')
        turtle_speed = random.randint(0, 10)
        t.forward(turtle_speed)

# exit
screen.exitonclick()