#########################
# 프로그램은 기본적으로 첫줄부터 차례대로 한줄씩 실행됨; 그러나 제어문을 사용하여 특정부분을 선택적으로 실행하거나 (if) 반복적으로 실행할 수 있음(for, while)
# if 문 : 조건에 따라서 실행코드를 다르게 지정함
# for 문 : 특정 부분을 조건이 만족할 때까지 반복실행함
# while 문 : 특정 부분을 조건이 만족할 때까지 반복실행함
#########################

# 변수의 값 검사 

a = 300
if ( a < 100 ) :
    print("a is less than 100")
    print('...더 많은 문장들이 나올 수 있음')
else :
    print("a is greater than 100")
    print('...더 많은 문장들이 나올 수 있음')
    
# 사용자가 입력한 데이터 검사 예제 

a = int(input('number: '))
if ( a < 100 ) :
    print("a={0} is less than 100".format(a))   # 양식을 사용한 출력 : 변수a의 값을 {0} 위치에 출력함 
else :
    print("a={0} is greater than 100".format(a))
    
# 사용자가 입력한 데이터 검사 예제 
# input() 함수는 문자열을 받아들이며 따라서 a < 100과 같이 수치비교를 할 수 없음 => int()로 변환해야 함 

a = int(input('number: '))
if ( a < 100 ) :
    print("a={0} is less than 100".format(a))   # 양식을 사용한 출력 : 변수a의 값을 {0} 위치에 출력함 
else :
    print("a={0} is greater than 100".format(a))