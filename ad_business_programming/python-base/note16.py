# 객체지향 언어는 문제를 '객체'와 '객체사이에 주고받는 메시지'로 모델링하여 해결하는 새로운 패러다임을 제공함
# 객체는 데이터 구조와 그 데이터에 적용하는 함수(명령어, 메소드)로 구성됨
# 프로그램에서는 문제를 객체 (데이터+함수)들로 모델링하고, 객체들 간에 메시지를 주고받는 형태로 모델링하여 해결함
# 예시 : 은행의 계좌에 대한 입금과 출금등을 처리하는 프로그램

class BankAccount:
    def __init__(self, name1, balance1):   # 객체가 생성될 때 실행되는 초기화 함수 
        self.name = name1
        self.balance = balance1
        print(self.name, "의 BankAccount 객체가 생성!")

    def withdraw(self, amount):
        self.balance -= amount
        print(self.name, "통장에서 ", self.amount, "원 출금")

    def deposit(self, amount):
        self.balance += amount
        print(self.name, "통장에 ", amount, "원 입금")

    def transfer(self, aa, amount):
        self.balance -= amount
        aa.balance += amount
        print(self.name, '의 통장에서', aa.name, '통장으로', amount, '원이 전달되었음' )

    def status(self):
        print(self.name, "현재 잔액 = ", self.balance)

# main program

print("Start")
a = BankAccount('홍길동', 2000)   # 객체 생성 
b = BankAccount('동길홍', 5000)
a.status()
b.status()

print()

a.transfer(b, 500)
a.deposit(1000)
a.status()
b.status()