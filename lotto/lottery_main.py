import random

def generate_numbers(n): 
    numbers = []
    
    while len(numbers) < n:
        num = random.randint(1, 45)
        if num not in numbers:
            numbers.append(num)
    return numbers

def draw_winning_numbers():
    draw_list = generate_numbers(7)
    return sorted(draw_list[:6]) + draw_list[6:]

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