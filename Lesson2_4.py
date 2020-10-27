string = input('Введите строку: ')
string = string.split()
for ind, el in enumerate(string):
    if len(el) < 10:
        print(ind, el)
    else:
        print(ind,el[:10])

