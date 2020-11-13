from time import sleep
from itertools import cycle
class TrafficLight:
    __color = [('Красный', 7), ('Желтый', 2), ('Зеленый', 10), ('Желтый', 2)]  # приватный атрибут(не доступен извне, нельзя исп. вне класса)
    def turn_on(self):
        for color, time in cycle (TrafficLight.__color):
            print(f"{color}, ожидание {time} секунд")
            sleep(time)
light_in_moscow = TrafficLight()
light_in_moscow.turn_on()





