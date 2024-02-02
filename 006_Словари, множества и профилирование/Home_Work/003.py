
#На входе:
# var1 = '5 4' # количество элементов первого и второго множества
var2 = '1 3 5 7 9' # элементы первого множества через пробел
var3 = '2 3 4 5' # элементы второго множества через пробел
# На выходе:
# 3 5
var_n = set(var2)

for _ in var_n:
    n = var_n 

var_m = set(var3)
for _ in var_m:
    m = var_m   

print()

res = sorted(n.intersection(m))
print(*res)



# n_1 = set(var2)
# print(n_1) 
# print(type(n_1))

 
# m_1 = set(var3)  
# print(m_1) 
# print(type(m_1)) 

# print()

# res = sorted(n_1.intersection(m_1))

# print(type(res))
# print(*res)
