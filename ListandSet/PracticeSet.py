class Set: # 집합 클래스
    def __init__(self): # 생성자
        self.items = [] # 원소를 저장하기 위한 리스트 생성
    
    def size(self): #집합의 크기
        return len(self.items) # len()함수 사용
    def display(self, msg): # 화면에 출력
        print(msg, self.items) # 메시지 + 집합 내용 출력
    def contains(self, item) :
        return item in self.items
    def contains(self, item) :
        for i in range(len(self.items)) :
            if self.items[i] == item :
                return True
        return False
    def insert(self, elem) :
        if elem not in self.items :
            self.items.append(elem)
    def delete(self, elem) :
        if elem in self.items :
            self.items.remove(elem)
    def union(self, setB):
        setC = Set()
        setC.items = list(self.items)
        for elem in setB.items :
            if elem not in self.items :
                setC.items.append(elem)
        return setC
    def intersect(self, setB) :
        setC = Set()
        for elem in setB.items :
            if elem in self.items :
                setC.items.append(elem)
        return setC
    def difference(self, setB) :
        setC = Set()
        for elem in self.items :
            if elem not in setB.items :
                setC.items.append(elem)
            return setC

setA = Set()
setA.insert('휴대폰')
setA.insert('지갑')
setA.insert('손수건')
setA.display('Set A : ')

setB = Set()
setB.insert('빗')
setB.insert('파이썬 자료구조')
setB.insert('야구공')
setB.insert('지갑')
setB.display('Set B : ')

setB.insert('빗')
setA.delete('손수건')
setA.delete('발수건')
setA.display('Set A : ')
setB.display('Set B : ')

setA.union(setB).display('A U B : ')
setA.intersect(setB).display('A ^ B : ')
setA.difference(setB).display('A - B : ')