class Point:

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y


array = []
first_pt = Point()
second_pt = Point()
third_pt = Point()
fourth_pt = Point()
fifth_pt = Point()
array_of_pt = [first_pt, second_pt, third_pt, fourth_pt, fifth_pt]

for i in range(5):
    x, y = map(int, input('Введите значения для {} экземпляра класса'.format(i +1)).split())
    array_of_pt[i].x = x
    array_of_pt[i].y = y

for i in range(5):
    print('вот x {}, а вот у {}'.format(array_of_pt[i].x, array_of_pt[i].y))

