import modul1

print(modul1.max_1(5, 9))

print('__вариант 2_______________________________')

from modul1 import max_1

print(max_1(5,9))

print(max_1(15,9))

print('__вариант 3_______________________________')

from modul1 import *# *возврощает все функции из модуля modul!

print(max_1(2,7))

print('__вариант 4_______________________________')

import modul1 as m1 # импортирую модуль modul1 как (as) m1

print(m1.max_1(51, 9))