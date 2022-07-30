# 반복문 내부에서만 사용할 수 있는 break와 continue 키워드
# 반복문을 벗어날 떄 사용 : break
i = 0

while True:
    print("{}번째 반복문입니다.".format(i))
    i += 1

    input_text = input("> 종료하시겠습니까?(y)")
    if input_text in ["Y", "y"]:
        print("반복을 종료합니다.")
        break

# 현재 반복을 중지하고, 다음 반복으로 넘어감 : continue
numbers = [5, 15, 6, 20, 7, 25]

for number in numbers:
    #number가 10보다 작으면 다음 반복으로 넘어감
    if number < 10:
        continue # continue 키워드가 실행될 겨우 21번째줄로 넘어가는 것이 아닌 다음 반복으로 넘어감
    print(number)