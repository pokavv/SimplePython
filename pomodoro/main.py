import time
import math
import winsound
from tkinter import *
from const import *

# Click start_btn to start timer
def clickStart():
    global repeat
    repeat += 1
    
    work = WORK_MIN // 2 # 25min
    short_break = SHORT_BREAK_MIN # 5min
    long_break = LONG_BREAK_MIN // 2 # 20min
    
    if repeat % 8 == 0:
        winsound.PlaySound('./pomodoro/stop-rest.wav', winsound.SND_ASYNC)
        countDown(long_break)
        title.config(text='BreakTime!', fg=PINK)
    elif repeat % 2 == 0:
        winsound.PlaySound('./pomodoro/stop-rest.wav', winsound.SND_ASYNC)
        countDown(short_break)
        title.config(text='BreakTime!', fg=RED)
    else:
        winsound.PlaySound('./pomodoro/coins.wav', winsound.SND_ASYNC)
        countDown(work)
        title.config(text='WorkHard!', fg=GREEN)

# Click reset_btn to reset timer
def clickReset():
    global repeat
    
    repeat = 0
    window.after_cancel(update_timer)
    canvas.itemconfig(timer_text, text='00:00')
    title.config(text='Reset!')
    check.config(text='')

# Countdown
def countDown(cnt):
    cnt_min = math.floor(cnt / 60) # floor: 정수 내림
    cnt_sec = cnt % 60
    
    # 초가 1자리일 경우 '00'초를 출력
    if cnt_sec < 10:
        cnt_sec = f'0{cnt_sec}'
    
    canvas.itemconfig(timer_text, text=f'{cnt_min}:{cnt_sec}')
    print(cnt)
    if cnt > 0:
        global update_timer
        update_timer = window.after(1000, countDown, cnt - 1) 
        # count down 기능을 위해 recursion 이용
        # after: 일정 대기시간 이후 정해진 동작 실행
    else:
        # 0이 되면 countDown()이 종료되는 것을 막기 위해 count가 0이 되었을 때 다시 clickStart() 실행
        clickStart()
        repeat_cnt = 0
        for _ in range(math.floor(repeat / 2)):
            repeat_cnt += 1
        check.config(text=f'Repeat\n{repeat_cnt}')

# UI
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

title = Label(text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 25, 'bold'))
title.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image_tomato = PhotoImage(file='./pomodoro/tomato.png')
canvas.create_image(100, 112, image=image_tomato)
timer_text = canvas.create_text(100, 130, text='Let\'s go!', fill='white', font=(FONT_NAME, 20, 'bold'))
canvas.grid(column=1, row=1)

start_btn = Button(text='Start', highlightthickness=0, command=clickStart)
start_btn.grid(column=0, row=2)

reset_btn = Button(text='Reset', highlightthickness=0, command=clickReset)
reset_btn.grid(column=2, row=2)

check = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, 'bold'))
check.grid(column=1, row=3)

window.mainloop()