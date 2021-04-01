# 1
class Point3D:
    x, y = [1, 2]

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def get(self):
        return self.x, self.y

    def convert(self):
        return self.x, self.y

    def setCoords(self, x, y):
        self.x = x
        self.y = y


pt1 = Point3D(2, 3)
print(pt1.__dict__)
print(pt1.convert())
pt1.setCoords(5, 16)
print(pt1.__dict__)


# 2
class Point:

    def __init__(self, point=None):
        if point is None:
            self.x = 0
            self.y = 0
        else:
            self.x = point.x
            self.y = point.y


p2 = Point()
p2.x = 16
p2.y = 12
p3 = Point(p2)

print(p3.__dict__)













