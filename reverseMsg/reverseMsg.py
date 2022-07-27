'''
2022.07.25
프로그램명: reverseMsg.py
설명:
문자열을 입력받으면 문자열을 거꾸로 출력하는 프로그램
'''
# 문자열을 인수로 하는 사용자 정의 함수 reverse 정의

def reverse(str):
    msg = len(str) # msg는 문자열의 길이(len)
    if msg == 1 :
        return str # 만약 문자열의 길이(msg)가 1일 경우엔 문자열 그대로 return
    return str[-1] + reverse(str[0:msg-1])

input_msg  = input("문자열 입력: ") # 문자열 입력받음 
print("원문장 : ", input_msg)
print("역문장 : ", reverse(input_msg))