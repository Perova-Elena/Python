# Пользователь вводит целое положит.число. Найдите самую большую цифру в числе.
# Используйте while и арифметич.операции.
number = int(input('Введите целое положительное число: '))
if number <= 0:
    print('Вы ввели не положительное число.')
if number > 0:
    max = 0
    a = number
    while a > 0:
        razryad = a % 10
        a = int(a / 10)
        if razryad > max:
            max = razryad
    print(f"Наибольшая цифра в числе {number} - {max}")
