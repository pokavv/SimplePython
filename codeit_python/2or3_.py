num = 1
total_sum = 0

while num < 1000:
    if num % 2 == 0 or num % 3 == 0:
        total_sum += num
    num += 1
print(total_sum)