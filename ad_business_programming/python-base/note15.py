# function - Arbitrary arguments

def my_function(*kids): # 포인터 : 해당 주소 공유
    print("The youngest child is " + kids[2])

# main program 
my_function("Emil", "Tobias", "Linus")

# function -  keyword arguments
# 인자이름 매칭 방식 vs. 인자 위치 매칭방식

def my_function(child3, child2, child1):
    print("The youngest child is " + child3)

# main program 
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")