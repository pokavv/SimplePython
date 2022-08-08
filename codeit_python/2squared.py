value = int(input("몇 제곱까지 할까요?: "))

for i in range(0, value + 1):
    print("2^{} =".format(i), 2**i)