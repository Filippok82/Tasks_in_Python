# 36. Задать массив, заполнить случайными положительными трёхзначными числами. Показать количество нечетных\четных чисел

from random import randint

arr=[randint(100,999)for x in range(10)]
print(arr)
even = 0
odd = 0 
for i in arr:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
 
print('четных: {}, нечетных: {}'. format (even, odd))



