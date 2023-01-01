fruits = ['apple', 'pear', 'orange', 'banana']

def makePie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print('fruit pie')
    else:
        print(fruit + ' pie')

makePie(4)
makePie(2)