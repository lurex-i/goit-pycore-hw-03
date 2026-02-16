# Розробіть функцію normalize_phone(phone_number), що нормалізує телефонні номери до стандартного 
# формату, залишаючи тільки цифри та символ '+' на початку.
# Функція приймає один аргумент — рядок з телефонним номером у будь-якому форматі та перетворює 
# його на стандартний формат, залишаючи тільки цифри та символ '+'. Якщо номер не містить міжнародного 
# коду, функція автоматично додає код '+38' (для України). Це гарантує, що всі номери будуть 
# придатними для відправлення SMS.

import re

clear_pattern = re.compile(r"[^\d+]")
inter_part_pattern = re.compile(r"(.*)(\d{10})")

def normalize_phone(phone_number):
    cleared_phone_num = re.sub(clear_pattern, "", phone_number)
    return re.sub(inter_part_pattern, r"+38\2", cleared_phone_num)


raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)