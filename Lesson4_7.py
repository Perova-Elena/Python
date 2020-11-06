"""Вывести факториалы первых n чисел"""
from math import factorial
from itertools import count
def fact():
    for el in count(1):
        yield factorial(el)
i = 1
n = int(input('Введите целое n: '))
for el in fact():  # Сгенерированное конечное значение факториала в функции fact()
    print(f"{i}! = {el}")
    if i == n:
        break
    i+=1

