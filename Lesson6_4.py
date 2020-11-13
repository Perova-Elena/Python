class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        print(f'{self.name} поехала')
    def stop(self):
        print(f'{self.name} остановилась')
    def turn_direction(self, direction):
        print(f'{self.name} повернула {direction}')
    def show_speed(self):
        print(f'текущая скорость {self.speed}')

class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Вы превысили скорость в городе!')

class SportCar(Car):
    def what_color(self):
        print(f'У {self.name} цвет кузова {self.color}')

class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('Вы превысили скорость в городе!')

class PoliceCar(Car):
    def is_police(self):
        if self.is_police == True:
            print(f'{self.name} полицейская')

sport_car = SportCar(350, 'Красная', 'Ferrari', False)
town_car = TownCar(180, 'Желтая', 'Volga', False)
work_car = WorkCar(80, 'Зеленая', 'UAZ', False)
police_car = PoliceCar(220, 'Синяя', 'Lada', True)

sport_car.show_speed()
town_car.show_speed()
work_car.show_speed()
police_car.show_speed()
work_car.turn_direction('направо')



