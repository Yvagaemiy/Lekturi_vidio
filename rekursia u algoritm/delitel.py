# Задача №35. Решение в группах
# Напишите функцию, которая принимает одно число и 
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое 
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes 

def prime(n):
    flag = True
    i = 2
    while i  < n and flag == True:
        if n % i == 0:
            flag = False
        i = i + 1
    if flag == True:
         return 'yes'
    else:
         return 'no'
    
n = int(input('Введите число: '))
print(prime(n))




