from random import random

n = int(input("Введите n = "))
def x(n):
    if n <= 0:
        return 0
    else:
        return 0.9 * x(n-1) + 0.43 * random()

x(n)
print(x(n))