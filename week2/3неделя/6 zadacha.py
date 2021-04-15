#  составление расписания на неделю: на вход лист дат и лист тем(

from random import randint, choice
list_themes = ['python', 'js', 'html', 'css', 'SQl', 'Oracle database', 'php', 'Ruby', 'swift', 'go', 'c++']
list_date = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
data = {}
for i in range(len(list_date)):
    data[list_date[i]] = [choice(list_themes) for i in range(randint(2, 4))]

for i in data.items():
    print(*i)



