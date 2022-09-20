# for 반복문
# continue : 가장 가까운 반복을 건너뜀
# break : 가장 가까운 반복을 종료함

# 중첩 반복문 - 두 리스트 값을 조회하는 예제 

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for i in adj:
    if i == 'big':
        continue
    else:
        for j in fruits:
            print(i, j)