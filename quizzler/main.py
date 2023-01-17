##########################################
'''
description = {
    project_name: quizzler
    language: python 3.11.0
    use_API: Trivia api
    source: udemy.com/course/best-100-days-python
}
'''
##########################################

from brain import QuizBrain
from ui import QuizInterface
from model import Question
import data

quiz_bank = []
for question in data.question_data:
    question_text = question['question']
    question_answer = question['correct_answer']
    new_question = Question(question_text, question_answer)
    quiz_bank.append(new_question)

quiz = QuizBrain(quiz_bank)
app_ui = QuizInterface(quiz)