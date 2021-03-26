#3 вариант 2задача
list_phone_number = ['+7912123456', '+7915213456', '+6915213456', '+4915213456', '+7915213456']
list_phone_number1 = []
for number_phone in list_phone_number:
    start_number = number_phone[0] + number_phone[1]
    if start_number != '+7':
        list_phone_number1.append(number_phone)

print(list_phone_number1)