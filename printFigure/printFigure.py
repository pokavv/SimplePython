'''
2022.07.25
프로그램명: printFigure.py
설명:
입력값을 받은 뒤 그 수만큼의 층을 쌓아 도형을 출력하는 프로그램
'''

# 삼각형
def Triangle():
    layer = int(input('삼각형 층수를 입력하시오: '))
    for i in range(1, layer+1):
        print("*" * i)

# 역삼각형
def RTriangle():
    layer = int(input('역삼각형 층수를 입력하시오: '))
    for i in range(1, layer+1):
        print("*" * (layer-i))

# 피라미드
def Pyramid():
    layer = int(input('피라미드 층수를 입력하시오: '))
    for i in range(1, layer+1):
        print(' ' * (layer-i), '*' * (2*i-1))

# 다시 입력하기
def reinput():
    print("잘못된 입력값입니다. 다시 입력하세요!")
    return figure

###################

# 무슨 도형 출력할지 입력값 받기

figure = str(input("어떤 도형을 입력하시겠어요?(T, RT, Py): "))

if figure == 'T' or figure == 't':
    Triangle()
elif figure == 'RT' or figure == 'rt':
    RTriangle()
elif figure == 'Py' or figure == 'py':
    Pyramid()
else:
    reinput()