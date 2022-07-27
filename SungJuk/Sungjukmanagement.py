'''
2022.07.26
프로그램명: Sungjukmanagement.py
설명: 먼저 학생수를 입력받고 입력받은 학생수만큼 이름, 번호, 국어, 영어, 수학, 물리점수를 입력받습니다.
      이후 각 학생의 점수에 따른 학점을 출력합니다.
'''

# 학생 수 입력
total_num = int(input("Please enter Total of Students: "))

# 학생 정보 입력(학생 수만큼 입력 반복)
stu_name = input("Student's name: ")
stu_num = int(input("Student's number: "))
kor = int(input("Korean Score: "))
eng = int(input("English Score: "))
math = int(input("Math Score: "))
phy = int(input("Physics Score: "))
score_sum = kor + eng + math + phy
average = score_sum / 4
blank = '%-2s' %''

def sungjuk():
    i = 0

    if average >= 90:
        grade = "A"
    elif 90 > average >= 80:
        grade = "B"
    elif 80 > average >= 70:
        grade = "C"
    elif 70 > average >= 60:
        grade = "D"
    else:
        grade = "F"

    
    print("==========================================================")
    print("이름    번호  국어  영어  수학  물리  총점    평균  학점")
    print("==========================================================")
    print(stu_name, blank, stu_num, blank, kor, blank, eng, blank, math, blank, phy, blank, sum, blank, average, blank, grade)

for i in range(total_num):
    sungjuk()