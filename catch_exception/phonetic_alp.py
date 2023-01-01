import pandas as pd

data = pd.read_csv('catch_exception/nato_phonetic_alphabet.csv')
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

def generate_phonetic():
    word = input('enter word: ').upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print('only letter in the alphabet please.')
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()