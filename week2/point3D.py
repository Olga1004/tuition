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

    def add_x(self, value):
        self.CoordX += value

    def add_y(self, value):
        self.CoordY += value

    def add_z(self, value):
        self.CoordZ += value

    def subtract_x(self, value):
        self.CoordX -= value

    def subtract_y(self, value):
        self.CoordY -= value

    def subtract_z(self, value):
        self.CoordZ -= value

    def multipl_x(self, value):
        self.CoordX *= value

    def multipl_y(self, value):
        self.CoordY *= value

    def multipl_z(self, value):
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