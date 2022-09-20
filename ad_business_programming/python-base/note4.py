# 두 개의 튜플을 결합하는 연산 :  + 
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

# 튜플은 읽기 전용 (readonly)이므로 원소값 변경이 불가함   
thistuple = ("apple", "banana", "cherry") 
thistuple[3] = "orange" # 튜플의 원소는 변경할 수 없음 (immutable)
print(thistuple)