# Щоб виграти головний приз лотереї, необхідний збіг кількох номерів на лотерейному білеті з числами, 
# що випали випадковим чином і в певному діапазоні під час чергового тиражу. Наприклад, необхідно вгадати 
# шість чисел від 1 до 49 чи п'ять чисел від 1 до 36 тощо.

# Вам необхідно написати функцію get_numbers_ticket(min, max, quantity), яка допоможе генерувати 
# набір унікальних випадкових чисел для таких лотерей. Вона буде повертати випадковий набір чисел у 
# межах заданих параметрів, причому всі випадкові числа в наборі повинні бути унікальні.

import random

def get_numbers_ticket(min, max, quantity):
    if(min < 1 or max >1000 or min > max or quantity < min or quantity > max):
        print("Input values should follow the rule: 1 <= min <= quantity <= max <= 1000")
        return []
    res_set = set()
    while(len(res_set) < quantity):
        res_set.add(random.randrange(min, max + 1))

    res_list = list(res_set)
    res_list.sort()
    return res_list


lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)

lottery_numbers = get_numbers_ticket(3, 9, 4)
print("Ваші лотерейні числа:", lottery_numbers)

lottery_numbers = get_numbers_ticket(1, 44, 8)
print("Ваші лотерейні числа:", lottery_numbers)