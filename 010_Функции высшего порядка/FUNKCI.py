print('Варианты режима (мод):'*2)
print('____a____'*3)
# 1. a – открытие для добавления данных.
#    ○ Позволяет дописывать что-то в имеющийся файл.
#    ○ Если вы попробуете дописать что-то в несуществующий файл, то файл
# будет создан и в него начнётся запись.

colors = ['red', 'green', 'blue']
data = open('file.txt', 'a') # здесь указываем режим, в котором будем работать
data.writelines(colors) # разделителей не будет
data.close()
# ● data.close() — используется для закрытия файла, чтобы разорвать
# подключение файловой переменной с файлом на диске.
# ● exit() — позволяет не выполнять код, прописанный после этой команды в
# скрипте.
# ● В итоге создаётся текстовый файл с текстом внутри: redbluedreen.
# ● При повторном выполнении скрипта redbluedreenredbluedreen — добавление
# в существующий файл, а не перезапись файлов.
with open('file.txt', 'w') as data:
    data.write('line 1\n')
    data.write('line 2\n')
print()
print('____r____'*3)
# 2. r – открытие для чтения данных.
#    ○ Позволяет читать данные из файла.
#    ○ Если вы попробуете считать данные из файла, которого не существует,
# программа выдаст ошибку.
path = 'file.txt'
data = open('file.txt', 'r')
for line in data:
    print(line)
data.close()

print('____w____'*3)
# 3. w – открытие для записи данных.
#    ○ Позволяет записывать данные и создавать файл, если его не
#     существует.
# Миксованные режимы:
colors = ['red', 'green', 'blue']
data = open('file.txt', 'w')
data.writelines(colors) # разделителей не будет
data.close()
# ● В итоге создаётся текстовый файл с текстом внутри: ‘redbluedreen’.
# ● В случае перезаписи новые данные записываются, а старые удаляются.

print('____w+____'*3)
# 4. w+
#     ○ Позволяет открывать файл для записи и читать из него.
#     ○ Если файла не существует, он будет создан.
print('____r+____'*3)
# 5. r+
#    ○ Позволяет открывать файл для чтения и дописывать в него.
#    ○ Если файла не существует, программа выдаст ошибку.