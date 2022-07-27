'''
2022.07.28
프로그램명: Car_SuperCar.py
설명:
Car클래스를 부모클래스로, SuperCar클래스를 자식클래스로 하는 프로그램
'''

class Car :
    def __init__(self, color, speed = 0) :
        self.color = color
        self.speed = speed
    def speedUp(self) : self.speed += 10 # 가속 동작: 속도 10 증가
    def speedDown(self) : self.speed -= 10 # 감속 동작: 속도 10 감

car1 = Car('black', 0) # 검정색, 속도 0
car2 = Car('red', 120) # 빨간색, 속도 120
car3 = Car('yellow', 30) # 노란색, 속도 30
car4 = Car('blue', 0) # 파랑색, 속도 0
car5 = Car('green') # 초록색, 속도 0 (디폴트 인수 사용)

car2.speedDown() # car2 감속: 속도 10 감소
car4.speedUp() #car4 가속: 속도 10 증가
car3.color = 'purple' # car3의 색상을 purple로 변경
car5.speed = 100 # car5의 속도를 100으로 변경

class SuperCar(Car) :
    def __init__(self, color, speed = 0, bTurbo = True) :
        super().__init__(color, speed) # 부모(Car)클래스의 생성자 호출
        self.bTurbo = bTurbo # 터보모드를 위한 변수 생성 및 초기화
    def __repr__(self):
        return self.speed
    def setTurbo(self, bTurbo = True) : # 터보모드를 On/Off하는 메소드
        self.bTurbo = bTurbo
    def speedUp(self) : # SuperCar의 SpeedUp. 메소드 재정의
        if self.bTurbo : # 터보 모드이면
            self.speed += 50 # 속도가 급속히(50) 증가됨
        else : # 터보 모드가 아니면
            super().speedUp() # 일반 자동차 속도
    def __repr__(self) :
        if self.bTurbo :
            return "[%s] [speed = %d] 터보모드" % (self.color, self.speed)
        else :
            return "[%s] [speed = %d] 일반모드" % (self.color, self.speed)
        
s1 = SuperCar("Gold", 0, True)
s2 = SuperCar("White", 0, False)
s1.speedUp()
s2.speedUp()
print("슈퍼카1:", s1) # 슈퍼카1: Gold, speed = 50 터보모드
print("슈퍼카2:", s2) # 슈퍼카2: White, speed = 10 일반모드