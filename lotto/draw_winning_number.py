import random

def generate_numbers(n): 
    numbers = []
    
    while len(numbers) < n:
        num = random.randint(1, 45)
        if num not in numbers:
            numbers.append(num)
    return numbers

print(generate_numbers(5))

def draw_winning_numbers():
    draw_list = generate_numbers(7)
    return sorted(draw_list[:6]) + draw_list[6:]
    
print(draw_winning_numbers())