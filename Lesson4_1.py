""" Запуск скрипта с параметрами"""  # Запускать в консоли из той же директории где скрипт!
# Как запускать с консоли, пример - C:.....Lesson_4>python Lesson4_1.py 10 5 30
import sys
name, production, rate, bonus = sys.argv  # Можно = map (float, sys.argv[1:]), а "name" убрать
salary = float(production) * float(rate) + float(bonus)  # float, т.к. данные заходят в str типе
print(f"Заработная плата = {salary}руб.")


