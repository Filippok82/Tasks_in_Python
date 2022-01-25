# 24. Найти кубы чисел от 1 до N

n = int(input('Введите n:'))
import math
def cube_numbers (n):
    for i in range(1,n+1):
        print (f'куб числа {i} =  {math.pow(i, 3)}')
    return n
print (cube_numbers(n))
