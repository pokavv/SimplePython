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