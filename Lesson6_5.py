class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print('Метод переопределен в Pen')

class Pencil(Stationery):
    def draw(self):
        print('Метод переопределен в Pencil')

class Handle(Stationery):
    def draw(self):
        print('Метод переопределен в Handle')

pen = Pen('Мягкий карандаш')
pencil = Pencil('Гелевая ручка')
handle = Handle('Перманентный маркер')

pen.draw()
pencil.draw()
handle.draw()