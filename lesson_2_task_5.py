def month_to_season(month):
    if month in [12, 1, 2]:
        return "Зима"
    elif month in [3, 4, 5]:
        return "Весна"
    elif month in [6, 7, 8]:
        return "Лето"
    else:
        return "Осень"

try:
    month_input = input("Введите номер месяца: ")
    month = int(month_input)

    if 1 <= month <= 12:
        result = month_to_season(month)
        print("Сезон:", result)
    else:
        print("ВВЕДИТЕ КОРРЕКТНОЕ ЗНАЧЕНИЕ (число от 1 до 12)")
except ValueError:
    print("ВВЕДИТЕ КОРРЕКТНОЕ ЗНАЧЕНИЕ (целое число от 1 до 12)")