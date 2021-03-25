class Clock:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    def __add__(self, other):
        return {'hours': self.hours + other.hours, 'minutes': self.minutes + other.minutes, 'seconds': self.seconds + other.seconds}
    def __sub__(self, other):
        return {'hours': self.hours - other.hours, 'minutes': self.minutes - other.minutes, 'seconds': self.seconds - other.seconds}
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
t3 = Clock.__add__(t1, t2)
t4 = Clock.__sub__(t1, t2)
t5 = Clock.__eq__(t1, t2)
t6 = Clock.__ne__(t1, t2)
print("Результат сложения: " + str(t3['hours']) + ":" + str(t3['minutes']) + ":" + str(t3['seconds']))
print("Результат вычетания: " + str(t4['hours']) + ":" +  str(t4['minutes']) + ":" + str(t4['seconds']))
if t5 == True:
    print("Равно")
else:
    print("Не равно")






