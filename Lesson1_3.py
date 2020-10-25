# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
n = int(input('Введите целое число от 0 до 9: '))
nn = 10*n+n
nnn = 100*n+10*n+n
summa = n + nn + nnn
print(f'{n} + {nn} + {nnn} = {summa}')


