arg1 = float(input('Введите первое число: '))
arg2 = float(input('Введите второе число: '))
arg3 = float(input('Введите третье число: '))
def my_func(arg1, arg2, arg3):
    """Возвращает сумму 2-х наибольших из 3-х веденных чисел"""
    list = [arg1, arg2, arg3]
    return sum(list) - min(list)
print(my_func(arg1, arg2, arg3))