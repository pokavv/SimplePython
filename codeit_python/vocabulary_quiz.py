with open('vocabulary.txt', 'r', encoding='utf-8') as f:
    for line in f:
        data = line.split(': ')
        kor = data[1].strip()
        eng_answer = data[0]
        
        Quiz = input(f"{kor}: ")
        if Quiz == eng_answer:
            print('맞았습니다!')
        else:
            print(f'아쉽습니다. 정답은 {eng_answer}입니다.')