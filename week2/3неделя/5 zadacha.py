# 5 задачка
# создание рандомных массивов словарей с ключами: дата, список тем (id, name)
import datetime
from random import randint, choice

themes = ['python', 'js', 'html', 'css', 'SQl', 'Oracle database']
result = []
for i in range(randint(1, 10)):
    date = {}
    time = datetime.datetime.today().strftime('%d/%m/%Y')
    names = dict(id=randint(0, 20),
                 names=[choice(themes) for i in range(randint(1, 3))])
    date['data'] = time
    date['themes'] = [names]
    result.append(date)

print(result)