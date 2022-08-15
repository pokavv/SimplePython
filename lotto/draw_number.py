import random

def draw_numbers(num):
    numbers = []
    while len(numbers) < num:
        n = random.randint(1, 45)
        if n not in numbers:
            numbers.append(n)
    print(numbers)

draw_numbers(5)