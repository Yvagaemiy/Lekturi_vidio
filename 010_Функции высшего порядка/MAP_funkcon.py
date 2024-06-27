print("___функция map___"*2)

# list_1 = [x for x in range(1, 20)]
# print(list_1)

# list_2 = list(map(lambda x : x + 10 , list_1))
# print(list_2)


def selekt(fn,colich): # это тоже самое что функция map
    return [fn(i) for i in colich]

data = " 13 2 5 17 45 9 45"
print(data)
data = list(map(int, data.split()))
print(data)

print("___функция fillter___"*2)

spis = [15,20,175,183]
res = list(filter(lambda x : x % 10 == 5, spis))
print(res)

print("___функция enumeret___"*2)

s = ['начало', 'середина','конец']
for nn, s in list(enumerate(s,1)):
    print(f"{nn} {s}")