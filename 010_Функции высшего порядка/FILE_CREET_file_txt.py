print('_____вариант с а режим________________________________')


# 1. a – открытие для добавления данных.
# ○ Позволяет дописывать что-то в имеющийся файл.
# ○ Если вы попробуете дописать что-то в несуществующий файл, то файл
# будет создан и в него начнётся запись.


# colors = ['red', '99999', 'blue']
# data = open('file.txt' , 'a')# здесь указываем режим , в котором будет работать
# data.writelines(colors) # раздилителей не будет
# data.close()

print('_____вариант с w режим________________________________')

# 3. w – открытие для записи данных.
# ○ Позволяет записывать данные и создавать файл, если его не
# существует.

# with open('file.txt','w') as data:
#     data.write('line  1 \n')
#     data.write('zferhrthbs \n')# писать только на английском!!!!!!!
# print()

print('_______вариант с r режим____________________________________')

path = 'file.txt'
data = open('file.txt', 'r')
for i in data:
    print(i)
data.close()