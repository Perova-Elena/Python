list = [50, 'phone', 300, 45.3, None, False]
for el in range(len(list)):   # len(list) - длина списка (количество элементов)
    print(f'"{list[el]}" - {type(list[el])}')  # Вывод всех типов

# Вывод типа элемента по его индексу списке по запросу пользователя:
index = int(input(f"'Введите номер элемента списка от 0 до {len(list)-1}': "))
print(f'"{list[index]}" - {type(list[index])}')