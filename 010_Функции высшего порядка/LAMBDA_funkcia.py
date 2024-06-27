




# def calkyl_2(a, b):
#     return a * b

# def maht(opereishan, peremennai_x, peremennai_y):
#     print(opereishan( peremennai_x, peremennai_y))
    
# def calkyl_1(a , b):
#         return a + b


# calkyl_1= lambda a , b : a + b 
# maht(calkyl_1, 5, 45)
# maht(lambda a , b : a + b, 5, 45)

# data = [1,2,4,13,12,44]
# res = list()
# for i in data:
#     if i %2 ==0:
#       res.append((i, i**2))
# print(res)
    



#мой вариант не работает

# def chet_kvadrat(spisik):
#     fn_lambda = [ i**2 for i in spisik if i % 2 == 0]
#     print(fn_lambda)
# data = [1,2,3,12,44]
# chet_kvadrat(data)
#вариант с видео рабочий
def selekt(fn,colich): # это тоже самое что функция map
    return [fn(i) for i in colich]

def were(fn, colich):
    return [i for i in colich if fn(i)]

data = [1,2,3,12,44]
res =  selekt(int, data)
print(res)
res = were(lambda x : x %2 ==0, res)
print(res)
res = selekt(lambda x : (x, x **2), res)
print(res)