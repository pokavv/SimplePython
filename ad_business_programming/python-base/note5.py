d = {
    '국어' : 10, 
    '영어' : 30, 
    '사회' : 50
}
print(d)

# 새로운 원소 (키와 값)를 추가함
d["과학"] = 70    
print(d)

# 딕셔너리 d에서 키가 '사회'인 원소의 '값'을 90 으로 변경함
d["사회"]= 90    
print(d)

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
mydict = thisdict.copy()  # dictionary 복사
print(mydict)
print(thisdict)

mydict['model'] = 'Lotte'
print(mydict)