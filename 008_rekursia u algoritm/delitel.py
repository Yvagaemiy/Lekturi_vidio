# Задача №35. Решение в группах
# Напишите функцию, которая принимает одно число и 
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое 
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes 
print('_______вариант из записи___________________')
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


print('_______вариант с симинара__1_________________')
def prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
        return True
    
num = int(input('Введите число: '))
print(prime(num))



print('_______вариант с симинара_2__________________')
def prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
        return True

def check_num(num) :

    if num.isdigit() and int(num) > 1:
        return True
    return False
   
num = input('Введите число: ')

while not check_num(num):
    print('не коректный набор')
    num = input('Введите число: ')

num = int(num)
print(prime(num))
print("yes" if prime(num) else 'no')

print('_______вариант с симинара_3__________________')

def prime(num):
    if num % 2 == 0 or num % 3 and num not in  (2,3):# оптимизация кода определяем корень тоисть середину
        return False
    
    for i in range(3, int(num ** 0.5) + 1 , 2):
      
        if num % i == 0:
            return False
        return True

def check_num(num) :

    if num.isdigit() and int(num) > 1:
        return True
    return False
   
num = input('Введите число: ')

while not check_num(num):
    print('не коректный набор')
    num = input('Введите число: ')

num = int(num)
print(prime(num))
print("yes" if prime(num) else 'no')
