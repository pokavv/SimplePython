score = [100, 90, 80, 70, 60]
score[2] = 100
score.append(90)
print(f'국 {score[0]} 영 {score[1]} 수 {score[2]} 사 {score[3]} 과 {score[4]} 체 {score[5]}')
print(f'총점 {sum(score)}, 평균점수 {sum(score) / len(score)}, 과목수 {len(score)}')