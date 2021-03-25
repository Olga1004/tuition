#3 вариант 2задача
list_phone_number = ['+7912123456', '+7915213456', '+6915213456', '+4915213456', '+7915213456']
list_index = []
for number_phone in list_phone_number:
    if number_phone.count('+7'):
        list_index.append(number_phone)
for index in list_index:
        list_phone_number.remove(index)

print(list_phone_number)