with open("new_file.txt", "w") as f_obj:
    while True:  # Бесконечный цикл
        stroka = input('Введите строку или нажмите Enter для выхода: ')
        if not stroka:  # Если нет контента. (У Ивана: if stroka=='' пустая строка)
            break
        f_obj.write(stroka + '\n')  # \n  - перенос на новую строку

