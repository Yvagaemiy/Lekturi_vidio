

from data_creet import name_data, surname_data, phone_data, address_data

def input_data():
#   pass                #пока пустая функция
    name    =  name_data()
    surname =  surname_data()
    phone   =  phone_data()
    address =  address_data()
    var = int(input(f"В каком формате записать данные\n\n"
    f"1 вариант: \n"
    f"{name}\n{surname}\n{phone}\n{address}\n"
    f"2 вариант: \n"
    f"{name};{surname};{phone};{address}\n"
    f" Выберите вариант: "))

    while var != 1 and var != 2:
        print('Вы ввели не правельное число ')
        var = int(input('Введите правельный вариант : '))

    if var == 1:
        with open('data_first_variant.csv ','a', encoding= 'utf - 8') as f:# 'a' записать данные а - 'as f' открываем как имя файла f
            f.write(f"{name}\n{surname}\n{phone}\n{address}\n\n")
    elif var == 2:
        with open('data_second_variant.csv ','a', encoding= 'utf - 8') as f:
            f.write( f"{name};{surname};{phone};{address}\n\n")

def print_data():
    print('Вывожу данные из 1 файла: \n')
    with open('data_first_variant.csv ','r', encoding= 'utf - 8') as f:  # "r" вывести данные
        data_first = f.readlines()
        data_first_list = []
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                data_first_list.append(''. join(data_first[j : i + 1]))
                j = i
        print(''.join(data_first_list))

    
    print('Вывожу данные из 2 файла: \n')
    with open('data_second_variant.csv','r', encoding= 'utf-8') as f:  # "r" вывести данные
        data_second = f.readlines()
        print(*data_second)



def print_data_1():# распечатать_контакт
   print('Вывожу данные из 1 файла: \n')
   with open('data_first_variant.csv','r',encoding='utf-8')as f:
    #    print('__________________')
    #    print(fail.read())
    #    print('__________________')
    data_first = f.read().rstrip().split('\n\n')
    for nn, contakt in enumerate(data_first, 1):
        print(f'{nn}. {contakt }\n')

    
   

