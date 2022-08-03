class ArrayList :
    def __init__(self): # 생성자
        self.items = []
    def insert(self, pos, elem) :
        self.items.insert(pos, elem)
    def delete(self, pos) :
        return self.items.pop(pos)
    def isEmpty(self) :
        return self.size() == 0
    def getEntry(self, pos) :
        return self.items[pos]
    def size(self) :
        return len(self.items)
    def clear(self) :
        self.items = []
    def find(self, item) :
        return self.items.index(item)
    def replace(self, pos, elem) :
        self.items[pos] = elem
    def sort(self) :
        self.items.sort()
    def merge(self, lst) :
        self.items.extend(lst)
    def display(self, msg='ArrayList : ') :
        print(msg, '항목수=', self.size(), self.items)

s = ArrayList()
s.display('파이썬 리스트로 구현한 리스트 테스트')
s.insert(0, 10); s.insert(0, 20); s.insert(1, 30)
s.insert(s.size(), 40); s.insert(2, 50)
s.display("파이썬 리스트로 구현한 List(삽입x5): ")
s.sort
s.display("파이썬 리스트로 구현한 List(정렬 후): ")
s.replace(2, 90)
s.display("파이썬 리스트로 구현한 List(교체x1): ")
s.delete(2); s.delete(s.size() - 1); s.delete(0)
s.display("파이썬 리스트로 구현한 List(삭제x3) ")
lst = [ 1, 2, 3 ]
s.merge(lst)
s.display("파이썬 리스트로 구현한 List(병합+3): ")
s.clear
s.display("파이썬 리스트로 구현한 List(정리 후): ")

def myLineEditor() : # 라인 편집기 주 함수
    list = ArrayList() # 리스트 객체 생성
    while True :
        command = input("[메뉴선택] i-입력, d-삭제, r-변경, p-출력, l-파일읽기, s-저장, q-종료 => ")

        if command == 'i' : # 삽입 연산
            pos = int(input(" 입력행 번호 : ")) # 삽입할 행 번호 입력
            str = input(" 입력행 내용 : ") # 삽입할 행 내용 입력
            list.insert(pos, str) # insert 메소드로 삽입
        elif command == 'd' : # 행 삭제
            pos = int(input(" 삭제행 번호 : ")) # 삭제할 행 번호 입력
            list.delete(pos) # delete 메소드로 삭제
        elif command == 'r' : # 행 내용 변경
            pos = int(input(" 변경행 번호 : ")) # 변경할 행 번호 입력
            str = input(" 변경행 내용 : ") # 변경할 행 내용 입력
            list.replace(pos, str) # replace로 변경
        elif command == 'q' : return
        elif command == 'p' :
            print('Line Editor')
            for line in range (list.size()) :
                print('[%2d]'%line, end='')
                print(list.getEntry(line))
            print()
        elif command == 'l' :
            filename = 'test.txt'
            infile = open(filename, "r")
            lines = infile.readlines()
            for line in lines:
                list.insert(list.size(), line.rstrip('\n'))
            infile.close()
        elif command == 's' :
            filename = 'test.txt'
            outfile = open(filename, "w")
            for i in range(list.size()) :
                outfile.write(list.getItem(i) + '\n')
            outfile.close()
myLineEditor()