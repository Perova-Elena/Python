from itertools import count, cycle
"""Итератор, генерирующий целые числа, начиная с указанного"""
num_begin = int(input('Введите целое число, с которого начать: '))
num_end = int(input('Введите целое число, которым закончить: '))
for el in count(num_begin):
    if el > num_end:
        break
    else:
        print(el)
"""Итератор, повторяющий элементы списка"""
i = 0
for el in cycle([1, 2, 3, 4]):
    if i > 9:
        break
    print(el)
    i+=1

