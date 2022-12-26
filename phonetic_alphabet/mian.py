import pandas as pd

data = pd.read_csv('./phonetic_alphabet/nato_phonetic_alphabet.csv')
data_dict = {row.letter:row.code for (index, row) in data.iterrows()}

user_input = []
for i in input('enter word: ').upper():
    user_input.append(i)

output = [data_dict[letter] for letter in user_input]
print(output)