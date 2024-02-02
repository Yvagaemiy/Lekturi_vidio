
# list1 = [1 ,2 , 3, 4, 5, 6, 15 , 23 , 38]
# list2 = list()
# for i in list1:
#     if i % 2 == 0:
#         list2.append((i, i ** 2))
# print(list2)

print('___Вариант №2_____________________________')

def select(funkcuo, znachenie):
    return [funkcuo(x) for x in znachenie]# возврощает список к каторому пременили функцию f от х

def were(funkcuo, znachenie):
    return [ x for x in znachenie if funkcuo(x) ]# возврощает в том случии если прошло проверку функцию f от х

list1 = [1 ,2 , 3, 4, 5, 6, 15 , 23 , 38]

res = select(int , list1)
print(res)

res = were(lambda x : x % 2 == 0 , res)
print(res)

res = list(select( lambda x : (x , x **2), res))
print(res)