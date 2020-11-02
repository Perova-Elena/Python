x = float(input('Введите действительное положительное число x: '))
y = int(input('Введите целое отрицательное число y: '))
if y >= 0 or x < 0:
    print('Вы ввели некорректные данные')
else:
    def my_func(x,y):
        """Возвращает x в степени y, способ-1 через **"""
        return x**y
    print('Способ 1: ', my_func(x, y))

    def my_func(x,y):
        """Возвращает x в степени y, способ-2 через цикл"""
        num = 1
        for i in range(abs(y)):
            num = x * num
        return 1 / num
    print('Способ 2: ', my_func(x, y))