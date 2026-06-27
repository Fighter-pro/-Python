def get_age_category(age):
    if age < 0:
        return "Некорректный возраст"
    if age < 18:
        return "Ребенок"
    if age < 65:
        return "Взрослый"
    return "Пенсионер"


def get_numbers_sum(numbers):
    result = 0

    for number in numbers:
        result += number

    return result


def get_best_seller(sales):
    if not sales:
        return None

    best_seller = max(sales, key=sales.get)
    return best_seller