import random

def generate_numbers(n): 
    numbers = []
    
    while len(numbers) < n:
        num = random.randint(1, 45)
        if num not in numbers:
            numbers.append(num)
    return numbers

print(generate_numbers(5))