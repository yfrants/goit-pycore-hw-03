from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    """
    Функція повертає список користувачів, у яких дні народження відбудуться протягом наступного тижня.
    Користувачі, у яких день народження припадає на вихідні, будуть перенесені на понеділок.

    Параметри:
    users (list): список словників з ключами "name" та "birthday" (формат "YYYY.MM.DD")

    Повертає:
    list: список словників з ключами "name" та "congratulation_date" (формат "YYYY.MM.DD")
    """
    upcoming_birthdays = []
    today = datetime.today().date()

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        birthday_this_year = birthday.replace(year=today.year)
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        if 0 <= (birthday_this_year - today).days < 7:
            congratulation_date = birthday_this_year
            if congratulation_date.weekday() == 5: 
                congratulation_date += timedelta(days=2)
            elif congratulation_date.weekday() == 6:
                congratulation_date += timedelta(days=1)

            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d"),
                })
        
    return upcoming_birthdays


users = [
    {"name": "Tony Stark", "birthday": "1985.10.23"},
    {"name": "Black Widow", "birthday": "1990.10.25"},
    {"name": "Steve Rogers", "birthday": "1980.10.31"}
]
upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)