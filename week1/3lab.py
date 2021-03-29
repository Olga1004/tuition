#1вариант 1 задача
class rectangle():
    def init(self, width,length):
        self.width = width
        self.length = length
    def area(self):
        return self.width * self.length

a = int(input("длина прямоугольника: "))
b = int(input("ширина прямоугольника: "))
obj = rectangle(a, b)
print("Площадь прямоугольника:", obj.area())
 