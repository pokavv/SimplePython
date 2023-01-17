from tkinter import *
from brain import QuizBrain

THEME_COLOR = '#375362'

class QuizInterface:
    
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title('Quizzler App')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        self.score_label = Label(text='Score: 0', fg='white', bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        
        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(
                                                    150, 125,
                                                    width=280,
                                                    text='Question Text', 
                                                    fill=THEME_COLOR,
                                                    font=('Arial', 12, 'italic')
                                                    )
        self.canvas.grid(row=1, column=0, columnspan=2,
                        pady=50)
        
        true_image = PhotoImage(file='quizzler/images/true.png')
        self.true_btn = Button(
                            image=true_image,
                            highlightthickness=0,
                            command=self.true_pressed
                            )
        self.true_btn.grid(row=2, column=0)
        
        false_image = PhotoImage(file='quizzler/images/false.png')
        self.false_btn = Button(
                                image=false_image,
                                highlightthickness=0,
                                command=self.false_pressed
                                )
        self.false_btn.grid(row=2, column=1)
        
        self.next_question()
        
        self.window.mainloop()
    
    def next_question(self):
        if self.quiz.still_questions():
            self.canvas.config(bg='white')
            self.score_label.config(text=f'Score: {self.quiz.score}')
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=question_text)
        else:
            self.canvas.itemconfig(
                                self.question_text,
                                text='Quiz End'
                                )
            self.true_btn.config(state='disabled')
            self.false_btn.config(state='disabled')
    
    def true_pressed(self):
        self.feedback(self.quiz.check_answer('True'))
    
    def false_pressed(self):
        is_right = self.quiz.check_answer('False')
        self.feedback(is_right)
    
    def feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.next_question) # 1 sec