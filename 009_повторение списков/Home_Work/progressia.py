# Заполните массив элементами арифметической прогрессии.
# Её первый элемент a1 , разность d и количество элементов n будет задано автоматически.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Пример
# На входе:
a1 = 2
d = 3
n = 4
# На выходе: 2 5 8 11


for i in range(n):
    print(a1 + i * d, end=' ')

print()
print('_______рабочая версия для автотестов____________________________________________')

a1 = 2
d = 3
n = 4
# Введите ваше решение ниже
for i in range(n):
    f = a1 + i * d
    print(f)