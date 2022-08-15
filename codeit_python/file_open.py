    # w : write, 파일 쓰기
with open('new_file.txt', 'w') as f:
    f.write("Hellow World!")
    f.write("new txt")
    
    # \n : 줄바꿈
with open('new_file.txt', 'w') as f:
    f.write("Hellow World!\n")
    f.write("new txt\n")
    
    # a : append, 기존 파일에 추가
with open('new_file.txt', 'a') as f:
    f.write("Hellow World!\n")
    f.write("new txt\n")