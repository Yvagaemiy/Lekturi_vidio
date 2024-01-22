def sum_chisel(n):
    summa = 0
    for i in range(1 , n + 1):
        summa = summa + i
    print(summa)
sum_chisel(int(input('Введите число: ')))