# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# На вход подается 2 числа через пробел: n m
# n - кол-во элементов первого множества.
# m - кол-во элементов второго множества.
# Затем подаются элементы каждого множества через пробел в виде строки. ! Писать input() не надо


print('___ВАРИАНТ С АВТОТЕСТОВ____________________________________--')


var1 = '5 4' 
var2 = '1 3 5 7 9' 
var3 = '2 3 4 5' 

# Введите ваше решение ниже


mol = [int(x) for x in var1.split()]
n = mol[0]
m = mol[1]
set_1 = set()
set_2 = set()
list_1 = list()
a = [int(x) for x in var2.split()]
k = set(a)
for i in k:
   set_1.add(i)
b = [int(x) for x in var3.split()]
k1 = set(b)
for i in k1:
   set_2.add(i)
lok = set_1 & set_2
kool = list(lok)
kool.sort()
for i in kool:
   print(i, end=' ')

print('____вариант мой_______________________________')

#На входе:
# var1 = '5 4' # количество элементов первого и второго множества
var2 = '1 3 5 7 9' # элементы первого множества через пробел
var3 = '2 3 4 5' # элементы второго множества через пробел
# На выходе:
# 3 5
var4 = set(var2)
var5 = set(var3)

for i in var2: 
    for j in var3:
      
        res_3 = var4.intersection(var5)
        res_4 = sorted(res_3)

print(*res_4)


print('___________________________________')    



from random import randint

n = {randint(1, 9) for _ in range(6)}
print(n)

m = {randint(1, 9) for _ in range(5)}
print(m)

res_1 = n.intersection(m)

print(res_1)


print('___множество не объяденины___________________________')
import  random

#n = int(input("Введите кол-во чисел множества: "))

for i in range(5):
    n_2 ={random.randint(1, 5)}
   
    print(n_2, end=' ') 

print('________________________________________________')

#m = int(input("Введите кол-во чисел множества: "))

for i in range(4):
    m_2 ={random.randint(1, 5)}
   
    print(m_2, end=' ')
print('__________________________________________________')
res = n_2.intersection(m_2) #пересечение множеств

print(res)




