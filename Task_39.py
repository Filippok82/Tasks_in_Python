# 39. Найти произведение пар чисел в одномерном массиве. Парой считаем первый и последний элемент,
#  второй и предпоследний и т.д.

from random import randint
from math import pow
m = int(input('количество чисел в массиве '))
arr = [randint(1, 20)for x in range(m)]
print(arr)
n = int(len(arr)/2)
a = []
if m % 2 == 0:
    for i in range(0, len(arr), n):
        a.append(arr[i:i + n])
        b = a[0]
        c = a[-1]
    c.reverse()
    for i in range(0, len(b)):
        print(b[i]*c[i])

else:
    print ('ввведите четное количество чисел ')
  







