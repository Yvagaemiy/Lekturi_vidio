print('__вариант 1___________________________')


def calkyl_1(a):
    return a + a


def calkyl_2(a):
    return a * a

def maht(opereishan, peremennai_x):
    print(opereishan(peremennai_x))

maht(calkyl_1, 5)

print('__вариант 2___________________________')




def calkyl_1(a, b):
    return a + b


def calkyl_2(a, b):
    return a * b

def maht(opereishan, peremennai_x, peremennai_y):
    print(opereishan(peremennai_x, peremennai_y))

maht(calkyl_2, 5, 10)