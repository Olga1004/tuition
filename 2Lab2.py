#3 вариант 2задача
list_phone_number = ['+7912123456', '+7915213456', '+6915213456', '+4915213456', '+7915213456']
list_phone_number1 = []
for number_phone in list_phone_number:
    start_number = number_phone[0] + number_phone[1]
    if start_number != '+7':
        list_phone_number1.append(number_phone)

print(list_phone_number1)
#дополнение

from random import randint
input_array = ['+' + ''.join([str(randint(5,9)) for i in range(10)]) for j in range(20)]

def random(list_phone_number):
    list_phone_number1 = []
    for number_phone in list_phone_number:
        start_number = number_phone[0] + number_phone[1]
        if start_number != '+7':
            list_phone_number1.append(number_phone)
    return list_phone_number1
print(input_array)
print(random(input_array))