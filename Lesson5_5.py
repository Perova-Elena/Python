with open('my_numbers.txt', 'w', encoding='utf-8') as file:
    numbers = input('Введите целые числа через пробел: ')  # Записались стрингом
    file.write(numbers + '\n')  # Записали введенный стринг в файл
    numbers = map(int, numbers.split())  # Присваиваем сразу всем элементам тип int
    summa = sum(numbers)
    file.write('Сумма ваших чисел равна: ' + str(summa))
    print('Сумма ваших чисел равна:', summa, '\n', 'Файл записан.')
