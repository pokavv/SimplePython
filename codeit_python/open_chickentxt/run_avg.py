with open('codeit_python/open_chickentxt/chicken.txt', 'r') as f:
    total = 0
    for line in f:
        lines = line.strip().split('일: ')
        total += int(lines[1])
    print(total / int(lines[0]))