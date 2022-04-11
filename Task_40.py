# 40. В Указанном массиве вещественных чисел найдите разницу между максимальным и минимальным элементом
from random import randint

arr=[randint(1,20)for x in range(10)]
print(arr)

a=min(arr)
b=max(arr)
res=b-a
print (f'\n минимальное {a} \n максимальное {b} \n разница {res}')