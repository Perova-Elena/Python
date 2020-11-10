import json
firm_dict = {}  # Пока пустой словарь с данными всех фирм
average_profit = []  # Пока пустой список средней прибыли
with open('Firms.txt') as file:
    lines = file.readlines()  # Считываем весь контент с файла Firms.txt, получаем list[ , , ]
    for line in lines:  # проходимся по каждой строке файла Firms.txt
        name, form, revenue, costs = line.split()  # Разбиваем каждую строку на части(слова) по пробелу
        profit = int(revenue) - int(costs)   # Считаем прибыль для каждой фирмы
        firm_dict[name] = profit  # Присваиваем названию фирмы(ключ) - прибыль
        if profit > 0:
            average_profit.append(profit)  # Добавляем положительную прибыль к списку рассчета средней прибыли
average_profit = sum(average_profit) / len(average_profit)  # Общая средняя прибыль = сумма прибыли \ число эл-тов списка
final_list = [firm_dict, {'average_profit': average_profit}]  # Итоговый список из 2х словарей
with open('firms.json', 'w') as file_json:  # Открываем для записи файл .json
    json.dump(final_list, file_json)  # Вызываем метод dump для загрузки в файл .json данных
with open('firms.json') as file_json:
    print(json.load(file_json))  # Проверка как записалось выгрузка методом load