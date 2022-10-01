from logo import logo
alp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#################

def caesar(txt, shift, direction):
    end_txt = ''
    if direction == 'decode':
        shift *= -1
    
    for i in txt:
        if i not in alp:
            new_ch = i
        else:
            posi = alp.index(i)
            new_posi = posi + shift
            
            if new_posi > len(alp) - 1:
                new_posi -= len(alp)
            elif new_posi < 0:
                new_posi += len(alp)
            new_ch = alp[new_posi]
        end_txt += new_ch

    print(f"Here's the {direction}d result: {end_txt}")
    re = input("Type 'yes' if you want to go again. Otherwise type 'no'. \n")
    if re == 'yes':
        cipher_bot()
    elif re == 'no':
        print('Exit')

#################

def cipher_bot():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
    txt = input('Type your message: ').lower()
    shift = int(input('Type the shift number: '))
    shift = shift % len(alp)
    caesar(txt, shift, direction)

#################

print(logo)
cipher_bot()