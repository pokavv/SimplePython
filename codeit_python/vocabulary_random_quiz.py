import random

with open('vocabulary.txt','r', encoding='utf-8') as f:
    vocab = {}
    for line in f:
        data = line.strip().split(": ")
        eng, kor = data[0], data[1]
        vocab[eng] = kor
    
dict_key = list(vocab.keys())
while True:
    index = random.randint(0, len(dict_key) - 1)
    eng = dict_key[index]
    kor = vocab[eng]
    
    user_input = input(f"{kor}: ")
    if user_input == 'q':
        break
    
    if user_input == eng:
        print('정답입니다!\n')
    else:
        print(f'아쉽습니다. 정답은 {eng}입니다.\n')