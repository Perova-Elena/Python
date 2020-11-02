divisible = float(input('Введите делимое: '))
divider = float(input('Введите делитель: '))
def  division_result(divisible, divider):
    """Возвращает частное от деления двух чисел"""
    try:
        return divisible / divider
    except ZeroDivisionError:
        print('Нельзя делить на ноль!')
        return
print(division_result(divisible, divider))
