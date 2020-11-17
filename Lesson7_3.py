class Cell:  # Создаем класс Клетка

    def __init__(self, nums):  # Инициализация - принимаем параметр  - количество мелких клеток внутри
        self.nums = nums

    def __str__(self):  # Перегрузка метода - переводим число в строку при обращении к нему от print()
        return str(self.nums)

    def __add__(self, other):  # Перегрузка метода вызывается при операции суммирования над экземплярами класса
        return 'Сумма клеточек = ' + str(self.nums + other.nums)

    def __sub__(self, other):  # Перегрузка метода вызывается при операции вычетания над экземплярами класса
        return self.nums - other.nums if self.nums > other.nums else 'Вычитание невозможно'

    def __mul__(self, other):  # Перегрузка метода вызывается при операции умножения над экземплярами класса
        return 'Произведение клеток =  ' + str(self.nums * other.nums)

    def __truediv__(self, other):  # Перегрузка метода вызывается при операции деления над экземплярами класса
        return 'Частное от деления клеток =  ' + str(round(self.nums / other.nums))

    def make_order(self, cols):  # Просто метод(функция), принимает сам объект(self) и число колонок cols
        return '\n'.join(['*' * cols for i in range(self.nums // cols)]) + '\n' + '*' * (self.nums % cols)  # Генераторное выражение создает целые ряды, и остаток от деления тот последний ряд, который не поместился

cell_1 = Cell(100)
cell_2 = Cell(61)
print(cell_1)  # Вызывает перегрузку метода __str__
print(cell_1 + cell_2)  # Вызывает перегрузку метода __add__
print(cell_1 - cell_2)  # Вызывает перегрузку метода __sub__
print(cell_1 * cell_2)  # Вызывает перегрузку метода __mul__
print(cell_1 / cell_2)  # Вызывает перегрузку метода __truediv__
print(cell_1.make_order(23))
print(cell_2.make_order(23))

