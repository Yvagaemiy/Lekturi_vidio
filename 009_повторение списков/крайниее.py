n = int(input("Введите длину массива: "))
array = list()
for i in range(n):
    x = int(input("Число : "))
    array.append(x)
    print(array)

count = 0
for i in range(1, n - 1):
    if array[i - 1] < array[i] > array[i + 1]:
       count +=1
print(count)            
