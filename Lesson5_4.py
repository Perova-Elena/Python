with open('numbers.txt') as file:  # режим 'r' по умолчанию. Для чтения не нужна кодировка UTF-8, т.к. текст на латинице
    lines = file.readlines()  # считываем все содержимое, заносится в list[]
with open('numbers_new.txt', 'w', encoding='utf-8') as file:
    for line in lines:  # Проходимся по элементам списка lines
        if '1' in line:
            line = 'Один - 1'
        elif '2' in line:
            line = 'Два - 2'
        elif '3' in line:
            line = 'Три - 3'
        elif '4' in line:
            line = 'Четыре - 4'
        file.write(line + '\n')  # \n чтобы запись шла с новой строки

