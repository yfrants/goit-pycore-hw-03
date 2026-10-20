import random

def get_numbers_ticket(min, max, quantity):
    """
    Функція генерує набір унікальних лотерейних чисел.
    Параметри:
    min (int): мінімальне число в діапазоні
    max (int): максимальне число в діапазоні
    quantity (int): кількість чисел у квитку
    Повертає:
    list: відсортований список унікальних чисел або порожній список у випадку помилки
    """

    if not (isinstance(min, int) and isinstance(max, int) and isinstance(quantity, int)):
        return []
    if min < 1 or max > 1000 or min > max:
        return []
    if quantity > (max - min + 1) or quantity < min:
        return []
 
    lottery_numbers_set = set()

    while len(lottery_numbers_set) < quantity:
        lottery_numbers_set.add(random.randint(min, max))

    return sorted(lottery_numbers_set)

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)