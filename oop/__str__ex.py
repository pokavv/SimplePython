class User:
    def __init__(self, name, email, pw):
        self.name = name
        self.email = email
        self.pw = pw
    
    def say_hello(self):
        print(f"안녕하세요! 저는 {self.name}입니다!")
    
    def __str__(self):
        return f"사용자: {self.name}, 이메일: {self.email}, 비밀번호: ******"

user1 = User("AAA", "AAA@AAA.kr", "123456")
user2 = User("BBB", "BBB@BBB.kr", "435234")

print(user1)
print(user2)