# function - 디폴트 인자 

def greet(name, msg="! 건강하세요?"):
    print("안녕 ", name + ', ' + msg)

# main program 
greet("영희")
greet("이순신", "감사합니다")

#########

# function - min, max 구하는 함수  

def max(a):
    i=0
    maximum = 0
    while a[i] > 0 :
        if a[i] > maximum :
            maximum = a[i]
        i=i+1
    return maximum

def min(a):
    i=0
    minimum = 100
    while a[i] > 0 :
        if a[i] < minimum :
            minimum = a[i]
        i=i+1
    return minimum

# main program 

salary = [10, 50, 40, 90, 45, 77, 100, 25, -1]

print("max = ", max(salary))
print("min = ", min(salary))