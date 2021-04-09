# 5 задачка
# создание рандомных массивов словарей с ключами: дата, список тем (id, name)
import datetime
from random import randint, choice

themes = ['python', 'js', 'html', 'css', 'SQl', 'Oracle database']
date = {}
hours = datetime.datetime.now().hour
minute = datetime.datetime.now().minute
time = str(hours) + ':' + str(minute)
tuple1 = tuple([randint(0, 20), choice(themes)])
tuple2 = tuple([randint(0, 20), choice(themes)])
date['data'] = time
date['themes'] = [tuple1, tuple2]
spisok = [date]
print(spisok)