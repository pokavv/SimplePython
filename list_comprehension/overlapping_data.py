with open('list_comprehension/file1.txt') as file1:
    text1 = file1.readlines()

with open('list_comprehension/file2.txt') as file2:
    text2 = file2.readlines()

overlapping = [int(num.strip()) for num in text1 if num in text2]
print(overlapping)