for x in range(2, 30, 3):
    print(x)

##################
# 구구단
num = int(input())

for i in range(1, num):
    print(f'---{i}단---')
    for j in range(1, num):
        print(f'{i} * {j} = {i * j}')