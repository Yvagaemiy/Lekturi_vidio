data = '2 23 156 46 4567 5 98'
# print(data)

# data = data.split()# строку переаодим в список
# print(data)

data = list(map(int, data.split()))# тоже вариант перевода листа строки в лист чисел
print(data)