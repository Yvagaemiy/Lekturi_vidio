print('______мой вариант_____________________________')

from random import randint
#list_1 = list(randint(1,9) for i in range(int(input("Введите количество кустов: "))))
#print(list_1)

# n = int(input('Введите массив № 1: '))

# for i in range(n):
#     array1 = randint(1, 10)
#     print(array1, end=' ')
array1 = set(randint(1, 10) for i in range(int(input('Введите массив №1: '))))
print(array1)

print()

array2 = set(randint(1, 10) for i in range(int(input('Введите массив №2: '))))
print(array2)

array3 = array1.difference(array2)# функция выводит то что есть в первом массиве но нет во втором и наоборот

print(array3)


print('______ вариант_ с лекции____________________________')

n = int(input('Введите длину массива:'))
list1 = list()
for i in range(n):
    x = int(input("Введите число: "))
    list1.append(x)
print(list1)  

m = int(input('Введите длину массива:'))
list2 = list()
for i in range(m):
    x = int(input("Введите число: "))
    list2.append(x)
print(list2)

count = 0
for i in range(n):
    for j in range(m):
        if list1[i] == list2[j]:
            count +=1
    if count == 0:
        print(list1[i])
    count ==0
