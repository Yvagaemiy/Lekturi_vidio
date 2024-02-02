n = int(input("Введите длину массива: "))
list1 = list()

for i in range(n):
    x = int(input("Число: "))
    list1.append(x)
    print(list1)

count = 0
for i in range(len(list1)):
    for j in range(i + 1 , len(list1)):
        if i != j and list1[i] == list1[j]:
            count +=1
print(count)