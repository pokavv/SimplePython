import random

chance = 4
answer = random.randint(1, 20)

while chance > 0:
    start = int(input("기회가 {}번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요:".format(chance)))

    if answer == start:
        print("축하합니다. {}번 만에 숫자를 맞히셨습니다.".format(chance))
        break
    else:
        chance -= 1
        if answer > start:
            print("Up")
        else:
            print("Down")

if chance == 0:
    print("아쉽습니다. 정답은 {}였습니다.".format(answer))
