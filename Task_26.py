# 26. Возведите число А в натуральную степень B используя цикл

a=int(input('Введите число a:'))
b=int (input('Введите число b:'))
def number(a):
    while a>0:
        return a**b
print(number(a))
