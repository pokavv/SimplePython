# 빈 리스트 만들기
numbers = []
print(numbers)

# numbers에 값들 추가
numbers.append(1)
numbers.append(7)
numbers.append(3)
numbers.append(6)
numbers.append(5)
numbers.append(2)
numbers.append(13)
numbers.append(14)
print(numbers)

# numbers에서 홀수 제거
i = 0
while i < len(numbers):
    if numbers[i] % 2 != 0:
        del numbers[i]
    # list는 요소가 제거되면 다음 요소들이 앞으로 끌어당겨지기 때문에 짝수일때만 i값 증가
    else:
        i += 1
print(numbers)

# numbers의 인덱스 0 자리에 20이라는 값 삽입
numbers.insert(0, 20)
print(numbers)

# numbers 정렬
numbers.sort()
print(numbers)
