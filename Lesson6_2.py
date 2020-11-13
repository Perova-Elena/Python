class Road:
    def __init__(self, length, width):  # Значения атрибутов (length,width) передаются в момент создания экземпляра, поэтому def __init__!!!
        self._length = length  # Ставим защиту(среднюю) на атрибуты (можно смотреть, нельзя использовать)
        self._width = width
    def calculation_of_massa(self):
        massa = self._length * self._width * 25 * 0.005  # Рассчет массы асфальта
        return massa
shosse = Road(5000, 20)  # Создаем экземпляр
print('Масса асфальта, (т.): ',shosse.calculation_of_massa())



















