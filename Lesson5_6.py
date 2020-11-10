dictionary = dict()
with open('Lessons.txt') as file:
    lines = file.readlines()  # Считываем все, получаем list[] из строк
    for line in lines:  # Проходимся по элементам списка lines
        broken_line = line.split()  # Разбиваем каждую линию на элементы по пробелу
        subject = broken_line[0]
        summa_of_hours = sum([int(el[:el.find('(')]) for el in broken_line[1:] if '(' in el])  # [] - Генератор часов для каждого предмета
        dictionary[subject[:-1]] = summa_of_hours
print(dictionary)