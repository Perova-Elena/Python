with open ('new_file.txt', 'r') as file:
    lines = file.readlines()  # получает 1 список строк [ , , ,...] (неразбитых по словам)
    number_of_lines = len(lines)  # Подсчет элементов списка
    print(f'Количество строк в файле new_file.txt - {number_of_lines}')
    for i, el in enumerate(lines):
        number_of_words = len(el.split())  # У Ивана , start = 1, чтобы отсчет шел не с 0
        print(f'{i+1}-я строка содержит {number_of_words} слова')
