from abc import ABC, abstractmethod  # Импортируем из модуля abc абстрактный класс ABC и абстрактный метод abstractmethod

class Clothes(ABC):  # Создаем австрактный класс
    def __init__(self, param):
        self.param = param

    @abstractmethod  # Следит за тем, чтобы у всех потомков обязательно был 1 метод calculate(self)
    def calculate(self):
        pass

class Coat(Clothes):

    @property  # Метод преобразован в свойство
    def calculate(self):
        return round((self.param / 6.5) + 0.5)

class Suit(Clothes):

    @property  # Метод преобразован в свойство
    def calculate(self):
        return round((2 * self.param) + 0.3)

coat = Coat(10)
suit = Suit(10)
print(coat.calculate)  # Обращение к методу calculate идет как к атрибуту без (), т.к. он преобразован в свойство с помощью @property
print(suit.calculate)  # Обращение к методу calculate идет как к атрибуту без (), т.к. он преобразован в свойство с помощью @property