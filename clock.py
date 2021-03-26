class Clock:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    def __add__(self, other):
        return Clock(self.hours + other.hours,  self.minutes + other.minutes, self.seconds + other.seconds)
    def __sub__(self, other):
        return Clock(self.hours - other.hours, self.minutes - other.minutes, self.seconds - other.seconds)
    def __convert__(hours, minutes, seconds):
        return hours * 60 * 60 + minutes * 60 + seconds
    def __eq__(self, other):
        time1 = Clock.__convert__(self.hours, self.minutes, self.seconds)
        time2 = Clock.__convert__(other.hours, other.minutes, other.seconds)
        return time1 == time2
    def __ne__(self, other):
        time1 = Clock.__convert__(self.hours, self.minutes, self.seconds)
        time2 = Clock.__convert__(other.hours, other.minutes, other.seconds)
        return time1 != time2
t1 = Clock(16, 20, 30)
t2 = Clock(9, 15, 26)
t3 = t1 + t2
print(t3)
t4 = t3 + t2
print(t4)
t5 = t1 - t2
print(t5)
t6 = Clock.__eq__(t1, t2)
t7 = Clock.__ne__(t1, t2)
print("Результат сложения: " + str(t3.hours) + ":" + str(t3.minutes) + ":" + str(t3.seconds))
print("Результат сложения: " + str(t4.hours) + ":" + str(t4.minutes) + ":" + str(t4.seconds))
print("Результат вычетания: " + str(t5.hours) + ":" +  str(t5.minutes) + ":" + str(t5.seconds))
if t6 == True:
    print("Равно")
if t7 != False:
    print("Не равно")
