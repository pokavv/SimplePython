'''
project name: mail_merge
date: 2022-12-24
description: A simple automation project that creates a new letter text file for each name by inserting the text of the invited names file into the text of the starting letter file as a variable.

'''
##########################################################################

PLACEHOLDER = '[name]'

with open('./mail_merge/Input/Names/invited_names.txt') as name_file:
    names = name_file.readlines()
    print(names)

with open('./mail_merge/Input/Letters/starting_letter.txt') as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, name)
        with open(f'./mail_merge/Output/ReadyToSend/letter_for_{name}.txt', mode='w') as will_send_letter:
            will_send_letter.write(new_letter)