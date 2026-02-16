# У межах вашої організації, ви відповідаєте за організацію привітань колег з днем народження. 
# Щоб оптимізувати цей процес, вам потрібно створити функцію get_upcoming_birthdays, яка допоможе 
# вам визначати, кого з колег потрібно привітати. Функція повинна повернути список всіх у кого 
# день народження вперед на 7 днів включаючи поточний день.

# У вашому розпорядженні є список users, кожен елемент якого містить інформацію про ім'я користувача 
# та його день народження. Оскільки дні народження колег можуть припадати на вихідні, ваша функція 
# також повинна враховувати це та переносити дату привітання на наступний робочий день, якщо необхідно.

from datetime import datetime
from datetime import date
from datetime import timedelta

def get_upcoming_birthdays(users):
    now = datetime.today().date()
    res_user_list = []
    for user in users:
        closest_bday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        closest_bday = date.replace(closest_bday, year=now.year)
        # Check if birthday is in the past already and move it in the future
        if((closest_bday - now).days < 0):
            closest_bday = date.replace(closest_bday, year=now.year + 1)
        # Check birthday is next 7 days includes today
        if((closest_bday - now).days < 7):
            #Correct congradulation day in case birthday is at weekend
            congr_day = closest_bday if closest_bday.weekday() < 5 else closest_bday + timedelta(days=7-closest_bday.weekday())
            res_user_list.append({"name":user["name"], "congratulation_date":congr_day.strftime("%Y.%m.%d")})

    return res_user_list



users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "John Doe1", "birthday": "1985.02.17"},
    {"name": "John Doe2", "birthday": "1985.02.21"},
    {"name": "John Doe3", "birthday": "1985.02.22"},
    {"name": "Jane Smith", "birthday": "1990.03.27"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)