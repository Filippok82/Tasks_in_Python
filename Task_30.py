# 30. Показать кубы чисел, заканчивающихся на четную цифру

n = int(input('Введите n:'))
import math
def cube_numbers (n):
    for i in range(1,n+1):
        if i%2==0:
            print (f'куб числа {i} =  {math.pow(i, 3)}')
    return i
print (cube_numbers(n))
