from datetime import datetime

def get_days_from_today(date: str):
    """
    Розраховує кількість днів між заданою датою і поточною.
    Повертає ціле число (від'ємне, якщо дата в майбутньому), або повідомлення про помилку, якщо формат дати не правильний. 
    """

    current_date = datetime.today().date()

    try:
        datetime_object = datetime.strptime(date, "%Y-%m-%d").date() 
    except ValueError:  
        return f"time data {date} does not match format '%Y-%m-%d'" 
    
    days_between = (current_date - datetime_object).days  

    return days_between

user_string_date = input("Enter a date (YYYY-MM-DD): ")

print(get_days_from_today(user_string_date))
