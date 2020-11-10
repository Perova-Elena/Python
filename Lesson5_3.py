with open('list_of_people.txt', 'r') as file:
    list_of_people = file.readlines()  # считывание всех строк файла
    sum = 0  # Сумма всех зарплат
    list_of_pour_people = []  # пока пустой список тех, у кого зп<20000
    for worker in list_of_people:
        last_name, salary = worker.split(':')  # Разбиваем каждую строку на 2 части
        salary = int(salary)  # Переводим зарплату из стринга в int
        sum += salary  # Считаем сумму всех зарплат (для подсчета средней)
        if salary < 20000:
            list_of_pour_people.append(worker)  # пополняем список тех, у кого зп<20000
    print("Список тех, кто мало зарабатывает: ", list_of_pour_people)
    average_salary = sum  / len(list_of_people)  # Рассчет средней зарплаты
    print("Средняя зарплата: ", average_salary)



