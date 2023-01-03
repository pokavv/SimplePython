import pandas as pd
from tkinter import *
import random

BG_COLOR = "#B1DDC6"
card = {}
learn = {}

try:
    data = pd.read_csv('flash_card/data/french_words.csv')
except FileNotFoundError:
    original = pd.read_csv('flash_card/data/french_words.csv')
    learn = original.to_dict(orient='records')
else:
    data_dict = data.to_dict(orient='records')

##################### Button event ##############################

def next_card():
    global card, timer
    window.after_cancel(timer) # timer 취소
    card = random.choice(data_dict)
    canvas.itemconfig(card_title, text='French', fill='black')
    canvas.itemconfig(word, text=card['French'], fill='black')
    canvas.itemconfig(card_background, image=card_front)
    timer = window.after(3000, func=flip_card) # timer 초기화

####################### Flip card ###############################

def flip_card():
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(word, text=card['English'], fill='white')
    canvas.itemconfig(card_background, image=card_back)

######################### is Known #############################

def is_known():
    data_dict.remove(card)
    learn = pd.DataFrame(data_dict)
    learn.to_csv('flash_card/data/words_to_learn.csv')
    next_card()

############################ UI #################################

window = Tk()
window.title('Flash Card')
window.config(padx=50, pady=50, bg=BG_COLOR)

timer = window.after(3000, func=flip_card) # 3000 after call flip_card()

canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file='flash_card/images/card_front.png')
card_back = PhotoImage(file='flash_card/images/card_back.png')
card_background = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 150, text='', font=('Ariel', 40, 'italic'))
word = canvas.create_text(400, 263, text='', font=('Ariel', 60, 'bold'))
canvas.config(bg=BG_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

x_image = PhotoImage(file='flash_card/images/wrong.png')
unknown = Button(image=x_image, highlightthickness=0, command=next_card)
unknown.grid(row=1, column=0)

check_image = PhotoImage(file='flash_card/images/right.png')
check = Button(image=check_image, highlightthickness=0, command=is_known)
check.grid(row=1, column=1)

next_card()

window.mainloop()