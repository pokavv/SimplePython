colors = ['red', 'green', 'gold']
colors

print('colors[0]= ', colors[0])
print('colors[-1]= ', colors[-1])
colors[-3]
colors[:] # 0번째~3번째 이전 원소까지
colors[1:2]
colors[:3]
colors[:-1] # 0번째~마지막 이전 원소까지

del colors[2]
colors

colors.append('blue')
print(colors)

colors.append('black')
print(colors)

print('pop(): ', colors.pop()) # 제거 후 제거요소 반환

idx = colors.index('red') # 'red' 원소의 list내 위치(인덱스) 출력

colors.insert(2, 'blue') # 특정위치에 값 삽입
print(colors)

colors.extend(['white', 'gray']) # 다른 리스트와 결합하여 확장
print('colors')

a = [10, 30, 5, 20, 90]
a.sort() # 정렬
a

colors.sort()
colors

alen = len(a) # 길이
print(a)
print(alen)