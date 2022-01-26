# 33. Задать массив из 12 элементов, заполненных числами из [-9,9].
# Найти сумму положительных/отрицательных элементов массива

from random import randint

def plus_minus(a):
    a=[randint(-9, 9) for i in range(a)]
    sum1 = sum2 = 0
    for i in a:
        if i > 0:
          sum1 += i
        else:
          sum2 += i
    return f'{a} \nсумма  положительных:{sum1} \nсумма отрицательных: {sum2}'
print (plus_minus(5))


