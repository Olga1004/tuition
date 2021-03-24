#1 вариант 2 задача
num = 4
factorial = 1
if(num%1==0 and num>=0):
    for i in range(1, num+1):
            factorial = i*factorial
    print(f'{num}! = {factorial}')
else:
    print("Нельзя вычислить факториал")
