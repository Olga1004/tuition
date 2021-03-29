# 1 лаб. 1задача 9 вариант
def my_function():
    for i in range(-4, 10):
        x = i/2
        for k in range(-6, 8):
            t = k/2
        if (x - t) ** 3 != 0:
            print(1 / ((x - t) ** 3) + 1)


my_function()


# 2 лаб. 1 задача
string = "abrakadabra"
print(string.replace("a", "A"))


# 2 лаб 2 задача
my_list = [1, 2, 0, -5, 7, 10, 234, -45, 3]
print('my_list', str(my_list))
diff_list = []
for i in range(1, len(my_list)):
    diff_list.append(my_list[i] - my_list[i-1])
print("differance list: ", str(diff_list))

# 3лаб. 1 зачада 10 вар.
import math
a = float(input("Введите сторону a: "))
b = float(input("Введите сторону b: "))
c = float(input("Введите сторону c: "))
s = math.sqrt(2 * (a * b + b * c + a * c))

print("Площадь параллелепипеда равна: ", s)

# 3 лаб. 2 задача 10 вар.
a = [15, 24, 47, 59, 61, 78, 90]
b = [4, 17, 31, 48, 59, 72, 83]
print([a_i - b_i for a_i, b_i in zip(a, b)])
