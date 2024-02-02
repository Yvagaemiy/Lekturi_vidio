# 0 1 1 2 3 5 8 13 21
def fubo(n):
    if n == 0 or n == 1:
        return 1
    return fubo(n - 1) + fubo(n - 2)
n = int(input('Введите место : '))
print('на ',n,'месте находится число:',fubo(n - 2))