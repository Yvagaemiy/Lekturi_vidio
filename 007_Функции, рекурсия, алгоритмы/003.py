def sum_str(*args): # "*" звесдочка дает принимать не огрониченное количество аргументов.
    res = ''
    for i in args:
        res = res + i
    return res
print(sum_str('r','g','g','h')) 
print(sum_str('r','g','g','h','a','z')) 
#print(sum_str(1,3,7))    