# call by value: 값만 전달 > 원래 변수 값 변하지 않음
# call by reference: 동일 주소를 공유 > 원래 변수 값 변함
    # 구조체는 call by reference

# 함수정의

def sum(i, j):
    valsum = 0;
    for k in range(i, j):
        valsum += k;
    return(valsum)

# main program (프로그램 시작은 여기부터)
print("<--> at main()/sum(1,10)=", sum(1,10)) # 함수 호출
print("<--> at main()/sum(1,20)=", sum(1,20))
print("<--> at main()/sum(1,30)=", sum(1,30))
print("<--> at main()/sum(1,100)=", sum(1,100))

#########

# function 정의 - call by value for single valued variable
# main/fruit 변수와 function/food는 값만 전달, 별개의 변수 (기억장소)

def my_function(food):
    print("in sub, 원래 food=", food,)
    food = 200
    print("in sub, 변경후 food=", food,)

# main program 
fruits = 100
my_function(fruits) # 함수 호출 (실행이 함수로 넘어감)
print("in main, fruits = ", fruits)

#########

# function 정의 - call by reference for list 
# 함수의 변수 (인자) food는 main의 리스트 fruits와 동일한 기억장소를 공유함 
# 구조체는 기억장소 공유, 단일값 변수는 값을 복사하여 사용

def my_function(food):
    print("in sub, food=", food)
    food[0] = "melon"

# main program 

fruits = ["apple", "banana", "cherry"]
my_function(fruits)
print("in main, fruits=", fruits)

#########