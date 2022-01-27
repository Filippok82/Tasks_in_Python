# 35. Определить, присутствует ли в заданном массиве, некоторое число

from random import randint
n = int(input('Введите число:'))


def element(arr):
    arr = [randint(1, 10) for i in range(arr)]
    print(arr)
    if n in arr:
        return True
    else:
        return False
print(element(10))
