i=0
whole_list = []
analis_name = []
analis_price = []
analis_quantity = []
analis_unit = []
while i >=0:
    i+=1
    name = str(input('Введите название товара: '))
    price = float(input('Введите цену товара: '))
    quantity = int(input('Введите количество товара: '))
    unit = str(input('Введите единицу измерения количества товара: '))
    dict = {'название':name, 'цена':price, 'количество':quantity, 'ед.':unit}
    list = (i, dict)
    whole_list.append(list)
    print(list)
    print(whole_list)
    if name in analis_name:
        checked_name = True
    else:
        analis_name.append(name)
    if price in analis_price:
        checked_price = True
    else:
        analis_price.append(price)
    if quantity in analis_name:
        checked_quantity = True
    else:
        analis_quantity.append(quantity)
    if unit in analis_unit:
        checked_name = True
    else:
        analis_unit.append(unit)
    analis_dict = {'название':analis_name, 'цена':analis_price, 'количество':analis_quantity, 'ед.':analis_unit}
    print(f"Аналитика: {analis_dict}")
