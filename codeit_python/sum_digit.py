# 자리수 합 리턴
def sum_digit(num):
    val = 0
    num_str = str(num)
    for i in num_str:
        val += int(i)
    return val

# sum_digit(1)부터 sum_digit(1000)까지의 합 구하기
i = 1
sum_1000 = 0
while i <= 1000:
    sum_1000 += sum_digit(i)
    i += 1
print(sum_1000)