def func_summa():
    exit = False
    result = 0
    while exit == False:
        entered_numbers = input('Введите строку чисел, разделенных пробелом или q для выхода: ').split()
        int_list = []
        summa = 0
        for el in entered_numbers:
            if 'q' == el:  # или 'q' in el / проверка на ввод спец символа на выход
                exit = True  # пора выходить
                break  # прерывает работу ближайшего цикла for, успев сложить элементы до 'q'
            el = int(el)  # перевод элеметов исходного списка из строчного типа в целые числа
            int_list.append(el)  # пополнение списка очередным целым числом
            summa = sum(int_list)  # подсчет суммы элементов промежуточного списка
        result = result + summa  # или result+=summa / суммирование конечной суммы с промежуточной
        print(result)
func_summa()


