# list comprehension

li = [1, 2, 3, 4]
new_list = [n + 1 for n in li]
print(new_list) # [2, 3, 4, 5]

name = 'Kolly'
name_li = [letter for letter in name]
print(name_li) # [K, o, l, l, y]

double = [num * 2 for num in range(1, 5)]
print(double) # [2, 4, 6, 8]

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
short_names = [name for name in names if len(name) < 5]
print(short_names)

long_names = [name.upper() for name in names if len(name) > 4]
print(long_names)