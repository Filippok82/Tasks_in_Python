# 23. Показать таблицу квадратов чисел от 1 до N 

n=int(input('Введите число n: '))
import math 
def tabl_sqrt(n):
    for i in range(1,n+1):
        print (f'квадрат числа {i} =  {math.pow(i, 2)}')
    return n
print(tabl_sqrt(n))        