# pавномерное распределение тем (цикл фор)

list_themes = ['python', 'js', 'html', 'css', 'SQl', 'Oracle database', 'php', 'Ruby', 'swift', 'go', 'c++']
list_date = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
data = {}
themes_per_day = len(list_themes) // len(list_date)
remaining_themes = len(list_themes) % len(list_date)

for i in range(len(list_date)):
    new_themes = i * themes_per_day
    data[list_date[i]] = list_themes[new_themes: new_themes + themes_per_day]
    if remaining_themes > 0:
        data[list_date[i]].append(list_themes[-1])
        remaining_themes -= 1


for i in data.items():
    print(*i)
