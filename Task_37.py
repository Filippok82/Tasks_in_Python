# 37.В одномерном массиве из 123 чисел найти количество элементов из отрезка [10,99]


from random import randint

arr=[randint(1,200)for x in range(12)]
print(arr)

count = sum(map(lambda x: x>10 and x<99, arr))
print(count)