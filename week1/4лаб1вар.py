import math
class complex:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return complex(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return complex(self.x - other.x, self.y - other.y)

a1 = complex(1, 2)
a2 = complex(3, 4)
print(a1 + a2)
print(a1 - a2)
a3 = a1.__add__(a2)
print(a3.x)



