class Worker:
    def __init__(self, name, surname, position, income):  # Поскольку передаются параметры нужна инициализация __init__
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income # на самом деле это словарь {'wage':wage, 'bonus':bonus}
class Position(Worker):  # Наследуем свойства класса Worker и добавляем свои методы
    def get_full_name(self):
        return f"{self.name} {self.surname} position {self.position}"
    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']
mr_smith = Position('Ivan', 'Smith', 'Dishwasher', {'wage':50000, 'bonus':3000 })
print(mr_smith.get_full_name())
print(mr_smith.get_total_income())








