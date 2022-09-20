a = {1, 2, 3, 4}
b = {3, 4, 5}
c = a.union(b) # 합집합
print(c)

d = a.intersection(b) # 중복값 출력
print(d)

# set difference 연산 
# set()을 생략해도 됨 

x = set({1,2,3,4,5})
y = set({3,4,5,6,7})
z = x-y              # set difference
w = x.difference(y)  # set difference
print(z)
print(w)

# symmetric_difference 연산은 공통원소를 제외한 나머지 원소들을 리턴함 

x = set({1,2,3,4,5})
y = set({3,4,5,6,7})
z = x.symmetric_difference(y) # 대칭차집합
print(z)

# 원소를 추가하는 연산 : add()

set_col = set({'Red','Blue','Green'})
print(set_col)
set_col.add('White')
print(set_col)

set_col = set({'Red','Blue','Green'})
print(set_col)
set_col.add('White')
print(set_col)

a, b = 10, 20   # (a, b) = (10, 20)와 동일한 의미이며, 변수 a와 b에 각각 10과 20을 저장함 
print(a, b)
print(a)

a, b = b, a   # 변수 a에 변수 b의 값을 저장하고, 변수 b에 변수 a의 값을 저장하라 (*** 두개를 동시에 꺼내서 동시에 저장함 ***)
print('a=', a, 'b=', b)