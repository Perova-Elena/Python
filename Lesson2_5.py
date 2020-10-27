# 1 способ (ввод списка через код):
list = [4, 8, 8, 8, 10, 10, 1, 2]
list.sort(reverse = True)
print('Рейтинг:')
for el in list:
    print(el, end=' ')

# 2 способ (ввод с клавиатуры):
list = []
a = int(input('Введите целое число > 0: '))
while a > 0:
    list.append(a)
    list.sort(reverse = True)
    print('Рейтинг:')
    for el in list:
        print(el, end=' ')
    a = int(input('Введите целое число > 0: '))













