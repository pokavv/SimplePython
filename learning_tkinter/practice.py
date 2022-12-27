import tkinter

def add(*args):
    print(args)
    n = 0
    for i in args:
        n += i
    return n

def cal(n, **kwargs):
    print(kwargs)
    for k, v in kwargs.items():
        print(k)
        print(v)
    print(kwargs['add'])
    print()
    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)

print(add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
cal(2, add=3, multiply=5)

################

class Car():
    
    def __init__(self, **kw):
        self.make = kw['make']
        self.model = kw['model']
        self.price = kw.get('price')

my_car = Car(make='Nissan', model='GT-R', price='14000')
print(my_car.model)
print(my_car.make)
print(my_car.price)