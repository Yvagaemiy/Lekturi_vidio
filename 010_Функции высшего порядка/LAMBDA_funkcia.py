




def calkyl_2(a, b):
    return a * b

def maht(opereishan, peremennai_x, peremennai_y):
    print(opereishan( peremennai_x, peremennai_y))
    
def calkyl_1(a , b):
        return a + b


calkyl_1= lambda a , b : a + b 
maht(calkyl_1, 5, 45)
maht(lambda a , b : a + b, 5, 45)