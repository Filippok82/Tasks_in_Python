#31. Задать массив из 8 элементов и вывести их на экран 

from random import randint
def creat_array(array):
    array = [randint(1,100) for i in range(array)]
    return array   
print (creat_array(8))


