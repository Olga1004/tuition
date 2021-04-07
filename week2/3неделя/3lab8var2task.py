# 3 лаб.8 вариант 2 задача
from random import random

n = int(input("Введите n = "))
def x(n):
    x = 1
    for i in range(n):
        yield x
        x = 0.9 * x + 0.43 * random()


print(list(x(n)))