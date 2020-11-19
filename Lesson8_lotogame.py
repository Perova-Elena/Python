from random import randint  # Импортируем модуль для генерации случайных чисел

def generate_numlist(quantity_of_numbers, min_keg, max_keg):  # Функция, генерирующая список случайных, но неповторяющихся! номеров для карточки в указанных пределах
    if quantity_of_numbers > max_keg - min_keg + 1:  # Проверяем не больше ли число номеров в карточке, чем число боченков в мешке
        raise ValueError('Заданы некорректные условия, число бочонков в мешке меньше, чем номеров в карточке')
    numlist = []  # Пустой список, который будем пополнять номерами
    while len(numlist) < quantity_of_numbers:  # Запускаем цикл с условием пока количество номеров меньше, чем нам надо, продолжай пополнять список
        new_number = randint(min_keg, max_keg)  # Получаем новое случайное число
        if new_number not in numlist:  # Проверяем, что нового случайного номера нет еще в списке номеров
            numlist.append(new_number)  # Пополняем список номеров для карточки
    return numlist  # Функция в итоге возвращает список случайных, но неповторяющихся! номеров для карточки

class Card:  # Класс Карта (у него потом будет 2 объекта: карта игрока и карта компьютера)
    rows = 3  # Задаем неизменные свойства(атрибуты) класса карты (число рядов = 3)
    cols = 9  # Задаем неизменные свойства(атрибуты) класса карты (число рядов = 9)
    nums_in_row = 5  # Задаем неизменные свойства(атрибуты) класса карты (число номеров в каждом ряду = 5)
    emptynum = 0  # Создаем переменную, обозначающую пустую клетку, присваиваем ей значение 0
    crossednum = -1

    def __init__(self):  # Конструктор класса Card

        quantity_of_numbers = self.nums_in_row * self.rows  # Считаем сколько всего номеров в карточке (по условию 15)
        numlist = generate_numlist(quantity_of_numbers, 1, 90)  # Генерируем список случайных, но неповторяющихся номеров для карточки
        self.card_list = []  # Итоговый список - карточка, заполненная номерами и пробелами

        for i in range(0, self.rows):  # Перебираем каждый ряд в карточке
            sorted_row = sorted(numlist[self.nums_in_row * i: self.nums_in_row * (i + 1)])  # Сортируем каждую 5-ку номеров случайного списка по возрастанию (0-5, 5-10, 10-15)
            empty_nums_count = self.cols - self.nums_in_row  # Считаем количество пустых клеточек в строке
            for j in range(0, empty_nums_count):  # В каждом ряду 4 раза (столько сколько пустых клеток) вставляем произвольно пустые клетки
                index = randint(0, len(sorted_row))  # Выбираем случайный индекс, куда вставим пустую клетку
                sorted_row.insert(index, self.emptynum)  # Вставляем пустую клетку в сортированный ряд
            self.card_list += sorted_row  # Пополняем итоговую карточку (полный список из 27 клеток)
    def __str__(self):  # Формируем вывод карточки на экран в стринговом формате
        dotted_line = '--------------------------'
        space = dotted_line + '\n'  # Линия + переход на новую строку
        for index, num in enumerate(self.card_list):  # Перебираем каждый элемент списка
            if num == self.emptynum:  # Если элемент = 0
                space += '  '  # Добавляем двойной пробел '  '
            elif num == self.crossednum:  # Если элемент = -1 (перечеркнут)
                space += ' -'  # Добавляем прочерк
            elif num < 10:  # Если элемент число<10
                space += f' {str(num)}'  # Записываем его с пробелом спереди, т.к. оно однозначное
            else:
                space += str(num)  # Иначе просто добавляем число в стринговом формате
            if (index + 1) % self.cols == 0:  # Условие перехода на новую строку карточки (переход через 9ю клеточку в нашем случае)
                space += '\n'
            else:
                space += ' '  # Если на новую строку переходить не пора, то добавляем после числа пробел, чтобы числа не сливались в карточке
        return space + dotted_line  # И замыкаем карточку еще одной пунктирной линией

    def __contains__(self, keg):  # Перегрузка оператора, вызывыется при проверке есть ли вытащенный из мешка бочонок в карточке
        return keg in self.card_list  # Возвращает булево значение Да или Нет

    def cross_num(self, keg):  # Функция, в которой вместо совпадающего с бочонком номера в карту вписывается -1
        for index, item in enumerate(self.card_list):
            if item == keg:  # Условие - если выпавший номер есть в карте, то:
                self.card_list[index] = self.crossednum  # Заменяем совпавший с бочонком номер на -1
                return

    def closed(self):  # Функция возвращает булево значение Да или Нет (закрыта ли полностью карточка)
        return set(self.card_list) == {self.emptynum, self.crossednum}  # Проверяет равно ли множество оствшихся номеров карты множеству из 0 и -1

class Game:

    numkegs = 90  # Задаем количество бочонков в мешке

    def __init__(self):  # Конструктор класса Игра (Game)
        self.usercard = Card()  # Создаем новую карту Игрока
        self.compcard = Card()  # Создаем новую карту Компьютера
        self.kegs = generate_numlist(self.numkegs, 1, 90)  # Генерируется мешок = список из 90 (по кол-ву боченков) неповторяющихся чисел в пределах от 1 до 90

    def play_game(self):  # Непосредственно ход самой игры

        keg = self.kegs.pop()  # Вытаскиваем бочонок из мешка
        print(f'Новый бочонок: {keg} (осталось {len(self.kegs)})')
        print(f'----- Ваша карточка ------\n{self.usercard}')
        print(f'-- Карточка компьютера ---\n{self.compcard}')
        useranswer = input('Зачеркнуть цифру? (y/n)').lower().strip()  # убираем пробелы до и после ответа и переводим в строчный регистр

        if useranswer == 'y' and not keg in self.usercard or \
           useranswer != 'y' and keg in self.usercard:
            return f'ComputerWon'

        if keg in self.usercard:
            self.usercard.cross_num(keg)
            if self.usercard.closed():
                return f'GamerWon'

        if keg in self.compcard:
            self.compcard.cross_num(keg)
            if self.compcard.closed():
                return f'ComputerWon'

        return f'GoOn'

game = Game()  # Создаем новый экземпляр игры

while True:
    status = game.play_game()
    if status == 'GamerWon':
        print('Вы выиграли')
        break
    elif status == 'ComputerWon':
        print('Вы проиграли')
        break