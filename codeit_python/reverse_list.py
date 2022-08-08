numbers = [2, 3, 5, 7, 11, 13, 17, 19]

# 리스트 뒤집기
for i in range(len(numbers) // 2):
    j = len(numbers) - i - 1
    num = numbers[i]
    numbers[i] = numbers[j]
    numbers[j] = num

print("뒤집어진 리스트: " + str(numbers))