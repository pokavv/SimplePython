def plus(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("1. Plus")
print("2. Subtract")
print("3. multiply")
print("4. Divide")
print()
cal = int(input("연산 선택: "))

num1 = input("첫 번째 숫자: ")
num2 = input("두 번째 숫자: ")

if cal == 1:
    print(num1, "+", num2, "=", plus(num1,num2))
elif cal == 2:
    print(num1, "-", num2, "=", subtract(num1,num2))
elif cal == 3:
    print(num1, "*", num2, "=", multiply(num1,num2))
elif cal == 4:
    print(num1, "/", num2, "=", divide(num1,num2))
else:
    print("Your input Wrong!")