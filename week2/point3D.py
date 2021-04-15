from scipy.spatial import distance

class CoordValue:
    def __set__(self, instance, value):
        self.value = value


class Point3D:
    CoordX = CoordValue()
    CoordY = CoordValue()
    CoordZ = CoordValue()
    def __init__(self, x = None, y = None, z = None):
        self.CoordX = x
        self.CoordY = y
        self.CoordZ = z

    def __add__(self, value):
        self.CoordX += value

    def __add__(self, value):
        self.CoordY += value

    def __add__(self, value):
        self.CoordZ += value

    def __sub__(self, value):
        self.CoordX -= value

    def __sub__(self, value):
        self.CoordY -= value

    def __sub__(self, value):
        self.CoordZ -= value

    def __mul__(self, value):
        self.CoordX *= value

    def __mul__(self, value):
        self.CoordY *= value

    def __mul__(self, value):
        self.CoordZ *= value

    def get_x(self):
        return self.CoordX

    def get_y(self):
        return self.CoordY

    def get_z(self):
        return self.CoordZ

    def coords(self):
        return self.CoordX, self.CoordY, self.CoordZ

    def getDistance(self, x1=0, x2=0, x3=0):
        first = (self.CoordX,self.CoordY,self.CoordZ)
        second = (x1,x2,x3)
        return distance.euclidean(first, second)