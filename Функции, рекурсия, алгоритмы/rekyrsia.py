def fubonach(n):
    if n in [1,2]:
        return 1
    return fubonach(n - 1) + fubonach(n - 2)
    
list1 = []

for i in range(1 , 10):
    list1.append(fubonach(i))
print(list1)    
