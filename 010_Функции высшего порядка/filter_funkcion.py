data = [3,4,56,7,89,98,654,5, 125, 575]

list_1 = list(filter(lambda x: x % 10 == 5 , data))

print(list_1)