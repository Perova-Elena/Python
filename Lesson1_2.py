# Пользователь вводит время в секундах. Переведите время в часы,
# минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
input_seconds = int(input('Введите время в секундах: '))
hours = input_seconds / (60 * 60)  # часы - точный результат с остатком
hh = int(hours)  # получим сколько целых часов
minutes = input_seconds % (60 * 60)  # получим сколько минут(выраженных в секундах) в остатке от часов
mm = int(minutes / 60)  # получим сколько целых минут(выраженных в минутах) в остатке от часов
ss = minutes % 60  # получим остаток, т.е. сколько секунд осталось от остатка минут
print(f"{input_seconds}сек. = {hh}:{mm}:{ss} (чч:мм:сс)")
