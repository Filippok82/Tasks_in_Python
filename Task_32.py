# 32. Задать массив из 8 элементов, заполненных нулями и единицами вывести их на экран 

from random import randint
def creat_zero_one (arr):
    arr=[randint(0,1)for i in range(arr)]
    return arr
print (creat_zero_one(8))


