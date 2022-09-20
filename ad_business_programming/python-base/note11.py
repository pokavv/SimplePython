i = 0
while i < 6:  # 0, 1, 2, 3, 4, 5
    i += 1      # i = i+1 의 축약형
    if i == 3:
        continue  # 이번 반복을 건너뜀 (8번 문장을 수행하지 않고, 4번 문장으로 가서 다음 번 반복수행)
    print(i)

####################

# 구구단
num = int(input())
i, j = 1, 1
while i < num + 1:
    print(f'---{i}단---')
    while j < num + 1:
        print(f'{i} * {j} = {i * j}')
        j = j + 1
    i = i +1
    j = 1