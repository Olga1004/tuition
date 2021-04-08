# 1 лаб.работа. 8 вариант. 1 задача

def my_function():
    for x in range(-2, 5, 1):
        # print(x, 'coord x')
        for t in range(-3, 4, 1):
            # print(t, 'coord t')
            if abs(x - t) != 0:
                print(1 / abs(x - t), 'result')


my_function()

# 1 лаб. 8 вар. 2 задача
num = input("Введите числа: ")
num = num.split(',')
min_number = [int(numbers) for numbers in num if int(numbers) > 0]

def is_number(num):
    try:
        int(num)
        return True
    except ValueError:
        return False


print(min(min_number))



# 2 лаб. 8 вариант 1 задача

stroka = 'abrakadabra'
print([i for i in range(len(stroka)) if stroka.startswith('ra', i)])

# 2 лаб. 8 вариант 2 задача
def sum(x):
    return x + 7.2

my_list = [-1, 0, 5, 3, 2]
print(list(map(sum, my_list)))

# lambda
my_list = [-1, 0, 5, 3, 2]
print(list(map(lambda x: x + 7.2, my_list)))
# list comprehesions
my_list = [x + 7.2 for x in (-1, 0, 5, 3, 2)]
print(my_list)

# 3 лаб. 8 вариант 1 задача
def euclidean_distance(x1, y1, x2, y2):
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5


print(euclidean_distance(15, 10, 40, 20))



#  4 лаб. 8 вариант

class Rub:
    def __init__(self, rubl, cop):
        if type(rubl) != int:
            raise TypeError('Rubl должен быть целым числом')
        if cop not in range(0,61):
            raise ValueError('Cop должен быть числом от 0 до 60')
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


inv1 = Rub(220, 6)
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