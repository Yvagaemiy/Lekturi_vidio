# Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.

# Функция не должна ничего выводить, только возвращать значение.

# Пример:

# sum(2, 2)
#    4

def sum1(a, b):
    if a ==  0 :
        return  b
    return sum1(a - 1 , b + 1)
a = int(input("Введите число а: "))
b = int(input("Введите число b: "))
print(sum1(a, b))