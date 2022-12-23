'''

project name: us-state-quiz
date: 2022-12-24
description: A simple program production project that fills in a blank map of the 50 states by matching the names of the 50 US states using the turtle and pandas library packages.

'''
############################################
import turtle
import pandas as pd

PATH = ('./us-state-map-quiz/data/50_states.csv')

screen = turtle.Screen()
screen.title('U.S. state quiz')
screen.setup(width=800, height=500)

img = './us-state-map-quiz/data/blank_states_img.gif'
screen.addshape(img)
turtle.shape(img)

df = pd.read_csv(PATH)
guessed = []
while len(guessed) < 50:
    all_states = df.state.to_list()
    answer_state = screen.textinput(title=f'{len(guessed)}/50 correct',
                                    prompt="What's another state's name?").title()
    
    if answer_state == 'Exit':
        missing_states = []
        for state in all_states:
            if state not in guessed:
                missing_states.append(state)

        learn = pd.DataFrame(missing_states)
        learn.to_csv('./us-state-map-quiz/state_to_learn.csv')
        break

    if answer_state in all_states:
        guessed.append(answer_state)
        txt = turtle.Turtle()
        txt.hideturtle()
        txt.penup()
        
        state_loc = df[df.state == answer_state]
        txt.goto(int(state_loc.x), int(state_loc.y))
        txt.write(answer_state)