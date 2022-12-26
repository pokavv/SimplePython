# new_dict ={new_key:new_value for item in list}
# new_dict ={new_key:new_value for (key, value) in dict.items()}
# new_dict ={new_key:new_value for (key, value) in dict.items() if test}
import random
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

scores = {student:random.randint(1, 100) for student in names}
print(scores)

passed_scores = {student:score for (student, score) in scores.items() if score >= 60}
print(passed_scores)