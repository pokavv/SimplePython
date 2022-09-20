# source: udemy.com/course/best-100-days-python

import random
from hangman_art import stages, logo
from hangman_words import word_list

print(logo)

life = len(stages) - 1
ur_choice = random.choice(word_list)
word_len = len(ur_choice)
game_over = False

display = []
for _ in range(word_len):
    display += '_'

while not game_over:
    play = input('Guess a letter: ').lower()
    
    if play in display:
        print(f"You've already guessed {play}")
    
    for i in range(word_len):
        alp = ur_choice[i]
        if alp == play:
            display[i] = alp
    print(f"{' '.join(display)}")
    
    if play not in ur_choice:
        print(f"You guessed {play}, that's not in the word. You lose a life")
        life -= 1
        if life == 0:
            game_over = True
            print(f'You lose. The Answer is {ur_choice}')

    if not '_' in display:
        game_over = True
        print('You Win!!!!!!!!!!!!!!!!!!')
    
    print(stages[life])