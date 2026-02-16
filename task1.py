# Створіть функцію get_days_from_today(date), яка розраховує кількість днів між заданою датою і поточною датою.
# Вимоги до завдання:
# Функція приймає один параметр: date — рядок, що представляє дату у форматі 'РРРР-ММ-ДД' (наприклад, '2020-10-09').
# Функція повертає ціле число, яке вказує на кількість днів від заданої дати до поточної. Якщо задана дата пізніша за поточну, результат має бути від'ємним.
# У розрахунках необхідно враховувати лише дні, ігноруючи час (години, хвилини, секунди).
# Для роботи з датами слід використовувати модуль datetime Python.

import datetime

def get_days_from_today(date:str):
    try:
        date_o = datetime.datetime.strptime(date, "%Y-%m-%d").date()
        now = datetime.date.today()
        return (now - date_o).days
    except:
        print("Date format should be YYYY-MM-DD")


# Test lines
# Invalid date input
res = get_days_from_today("2026-11-40")
print(res)
# 1 day till today ()
res = get_days_from_today("2026-02-14")
print(res)
# 1 day after today ()
res = get_days_from_today("2026-02-16")
print(res)
print(type(res))