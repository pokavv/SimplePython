# 사각형 클래스 생성 사각형 클래스를 정의 : 데이터는 가로, 세로 두가지, 메소드는 area를 계산하는 함수와 기존 사각형의 가로 및 세로 길이를 재설정하는 resize() 함수를 구현함 사각형 2개를 만들어 테스트

class rect:
    def __init__(self, name, width, height):
        self.name = name
        self.width = width
        self.height = height
        print(f'가로 {self.width}, 세로 {self.height}의 사각형 {self.name} 생성')

    def calc_area(self):
        print(f'{self.name} area = {self.width * self.height}')

    def resize(self, width, height):
        self.width = width
        self.height = height

ob_num = 0
a = rect('rect1', 5, 5)
ob_num += 1
b = rect('rect2', 2, 5)
ob_num += 1

a.calc_area()
b.calc_area()
a.resize(10, 20)
a.calc_area()
print(f'현재 사각형 객체의 개수 = {ob_num}')