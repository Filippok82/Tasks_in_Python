# 38. Найти сумму чисел одномерного массива стоящих на нечетной позиции

from random import randint

arr=[randint(1,20)for x in range(10)]
print(arr)
result = sum([x for x in arr if x % 2 != 0])
print(result)