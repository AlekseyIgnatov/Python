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
    
# Функция заполнения массива числами арифметической прогрессии
def arif_progr(a1,d,n):
    an = [a1+(i)*d for i in range(n)]
    return an

# Функция поиска индексов чисел массива попадающих в указанный диапазон
def index_mas(List, mind, maxd):
    List_ind=[]
    for i in range(len(List)):
        if List[i] >= mind and List[i] <= maxd:
            List_ind.append(i)
    return List_ind

# Функция вывода таблицы умножения
def print_operation_table(operation, num_rows=6, num_columns=6):
    List = [[(i+1)*(j+1) for i in range(num_rows)] for j in range(num_columns)]
    for row in List:
        print (' '.join(map(str, row)))
