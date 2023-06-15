# Функция возведения числа А в степень В используя рекурсию.

def stepen(a,b):
    if b==1:
        return a
    if b!=1:
        return (a*stepen(a,b-1))

# Функция сложения двух чисел А и В используя рекурсию.   
def sum(a,b):
    print(a,b)
    if b==0:
        return a
    else: 
        return sum(a+1,b-1)