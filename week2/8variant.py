# 1 лаб.работа. 8 вариант. 1 задача

def my_function():
    for i in range(-2, 5):
        x = i/1
        for j in range(-3, 4):
            t = j/1
        if abs(x - t) != 0:
            print(1 / abs(x-t))


my_function()

# 1 лаб. 8 вар. 2 задача

num = input("Введите числа: ")
num = num.split(',')
print(min(num))

# 2 лаб. 8 вариант 1 задача

import re
print([i.start () for i in re.finditer('(?=ra)', 'abrakadabra')])

# 2 лаб. 8 вариант 2 задача

my_list = [-1, 0, 5, 3, 2]
for x in range(5):
    my_list[x] += 7.2

print(my_list)

# 3 лаб. 8 вариант 1 задача
from scipy.spatial import distance
x = (10, 15) # подставлять значения для проверки
y = (13, 18)
dst = distance.euclidean(x, y)
print(dst)

#  4 лаб. 8 вариант

class Rub:
    def __init__(self, rubl, cop):
        self.rubl = rubl
        self.cop = cop

    def __add__(self, value):
        return Rub(self.rubl + value.rubl, self.cop + value.cop)

    def __sub__(self, value):
        return Rub(self.rubl - value.rubl, self.cop - value.cop)

    def __mul__(self, value):
        return Rub(self.rubl * value.rubl, self.cop * value.cop)


    def __gettatr__(self, value):
        sum = self + value
        return str(sum.rubl) + " руб." + str(sum.cop) + " коп."


inv1 = Rub(220, 8)
inv2 = Rub(180, 2)
inv3 = inv1 + inv2
print(inv3)
inv4 = inv1 - inv2
print(inv4)
inv5 = inv1 * inv2
print(inv5)
print("Результат сложения: " + str(inv3.rubl) + "," + str(inv3.cop))
print("Результат вычитания: " + str(inv4.rubl) + "," + str(inv4.cop))
print("Результат умножения: " + str(inv5.rubl) + "," + str(inv5.cop))
inv6 = Rub.__gettatr__(inv1, inv2)
print(inv6)
