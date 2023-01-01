# catch exception

try:
    file = open('catch_exception/file.txt')
    
    dict_a = {'key' : 'value'}
    print(dict_a['key'])
except FileNotFoundError:
    file = open('catch_exception/file.txt', 'w')
    file.write('something')
except KeyError as error_message:
    print(f'That key {error_message} does not exist.')
else:
    content = file.read()
    print(content)
finally: # raise: 자신만의 예외 생성
    raise TypeError('This is an error that I made up.')