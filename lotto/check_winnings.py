def count_matching_numbers(numbers, winning_numbers):
    n = 0
    for i in range(0, len(numbers)):
        for j in range(0, len(winning_numbers)):
            if numbers[i] == winning_numbers[j]:
                n += 1
    return n

def check(numbers, winning_numbers):
    num = count_matching_numbers(numbers, winning_numbers)
    
    if num == 6 and winning_numbers[6] not in numbers:
        return 1000000000
    elif num == 6 and winning_numbers[6] in numbers:
        return 50000000
    elif num == 5:
        return 1000000
    elif num == 4:
        return 50000
    elif num == 3:
        return 5000
    else:
        return 0


# 테스트
print(check([2, 4, 11, 14, 25, 40], [4, 12, 14, 28, 40, 41, 6]))
print(check([2, 4, 11, 14, 25, 40], [2, 4, 10, 11, 14, 40, 25]))