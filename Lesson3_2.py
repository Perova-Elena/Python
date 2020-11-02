def personal_info(name, surname, birth_year, live_town, email, phone):
    """Выводит на экран личные данные пользователя"""
    print(f"Данные пользователя: имя: {name};"
          f" фамилия: {surname}, "
          f"год рождения: { birth_year}, "
          f"город проживания: {live_town}, "
          f"email: {email},"
          f" телефон: {phone}")
personal_info(name = str(input('Введите Ваше имя: ')),
surname = str(input('Введите Вашу фамилию: ')),
birth_year = int(input('Введите Ваш год рождения: ')),
live_town = str(input('Введите город Вашего проживания: ')),
email = str(input('Введите Ваш email: ')),
phone = str(input('Введите Ваш телефон: ')))