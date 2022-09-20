people = {1: {'name': 'John', 'age': '37', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '32', 'sex': 'Female'}}

print(people[1]['name'])
print(people[1]['age'])
print(people[1]['sex'])
print()

###########

score_dic = {'국어' : 80, '영어' : 90, '수학' : 100, '사회' : 90, '과학' : 80}
score_dic['체육'] = 90
sum_score = score_dic['국어'] + score_dic['영어'] + score_dic['수학'] + score_dic['사회'] + score_dic['과학']

print(score_dic)
print(f'총점: {sum_score}, 평균: {sum_score / 5}')
print(f'최고점수: {max(score_dic)} {score_dic.get(max(score_dic))}, 최저점수: {min(score_dic)} {score_dic.get(min(score_dic))}')