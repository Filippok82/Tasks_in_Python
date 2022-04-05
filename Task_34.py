# 34. Написать программу замену элементов массива на противоположные
from random import randint
def change_elements (array):
    array=[randint(-10,10) for i in range(array)]
    print (array)
    for i in array:
        array[i]=array[i]*-1       
    return array
print(change_elements(10))



