# pавномерное распределение тем (цикл фор)

from random import randint, choice
list_themes = ['python', 'js', 'html', 'css', 'SQl', 'Oracle database', 'php', 'Ruby', 'swift', 'go', 'c++']
list_date = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
data = {}
themes_per_day = len(list_themes) // len(list_date)
remaining_themes = len(list_themes) % len(list_date)

for i in range(len(list_date)):
    data[list_date[i]] = [choice(list_themes) for i in range(themes_per_day)]
    if remaining_themes > 0:
        data[list_date[i]].append(list_themes[randint(0, len(list_themes))])
        remaining_themes -= 1

for i in data.items():
    print(*i)