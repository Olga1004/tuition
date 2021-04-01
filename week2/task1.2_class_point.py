#1
class Point3D:

    def __init__(self, x, y):
        self.xy = [x, y]

    def get(self):
        return tuple(self.xy)

    def setCoords(self, x, y):
        self.xy = [x, y]

#
pt1 = Point3D(2, 3)
print(pt1.__dict__)
print (pt1.get())
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













