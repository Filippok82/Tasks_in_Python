# 29. Написать программу вычисления произведения чисел от 1 до N
# a = 1
# for i in range(1,15):
#     a = a * i
#     print(a)





# def factorial(n):
#     if n == 0:                     # Решение с помощью рекурсии
#         return 1
#     else:
#         return factorial(n-1) * n 
 
# print(factorial(3))


# import math
# n=int(input('Введите число n: '))

# def factorial(n):              # Решение с помощью модуля Math
#     return math.factorial(n)
# print (factorial(n))



n = int(input('Введите n:'))
 
def factorial (a):
    for i in range(1, n+1):
         a=a*i
    return a
print(factorial(1))