# Задача №51. Решение в группах
# Напишите функцию same_by(characteristic, objects), которая 
# проверяет, все ли объекты имеют одинаковое значение 
# некоторой характеристики, и возвращают True, если это так. 
# Если значение характеристики для разных объектов 
# отличается - то False. Для пустого набора объектов, функция 
# должна возвращать True. Аргумент characteristic - это 
# функция, которая принимает объект и вычисляет его 
# характеристику.
# Ввод: Вывод:
# values = [0, 2, 10, 6] 
# if same_by(lambda x: x % 2, values):
# print(‘same’)
# else:
# print(‘different’)
def same_by(cfsgrthrt, sdvzdfgt):
    result = True
    list1 = [cfsgrthrt(x) for  x in sdvzdfgt]
    for i in range(len(list1) - 1):
        if list1[i] != list1[i + 1]:
            return False
    return result

v = [2,4,6,8]
if same_by(lambda x : x % 2 == 0 , v):
    print('same')
else:
    print('different')