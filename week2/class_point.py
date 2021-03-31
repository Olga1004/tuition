class Point3D:
    x = 2
    y = 5
    z = 8

pt = Point3D()

ss = Point3D()

Point3D.x = 25
print(Point3D.x)
print(pt.x, pt.y, pt.z)
print(ss.x, ss.y, ss.z)


delattr(Point3D, 'z')
print(Point3D.__dict__)
print(hasattr(pt, 'z'))
print(hasattr(ss, 'z'))
print(pt.x, pt.y)
print(ss.x, ss.y)



pt.y = 27
ss.x = 99
print(pt.__dict__)
print(ss.__dict__)