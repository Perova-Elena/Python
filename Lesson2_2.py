list = input('Введите элементы через пробел, затем нажмите ENTER: ').split()
print(f"Было: {list}")
for i in range(1, len(list), 2):
    list[i-1], list[i] = list[i], list[i-1]  #меняем местами соседние элементы
print(f"Стало: {list}")
