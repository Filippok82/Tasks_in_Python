# 11.Дано число из отрезка [10, 99]. Показать наибольшую цифру числа
# from random import randint
# a=(randint(10,100))
# print(a)
# c=a%10
# b=(a-c)//10                              # Решение без метода
# if b>c:
#     print (f'Наибольшая цифра {b}')
# else:
#     print (f'Наибольшая цифра {c}')


from random import randint
a=(randint(10, 100))
print(a)
def max_element (a):
    c=a%10
    b=(a-c)//10
    if b>c:
        return f'Наибольшая цифра {b}'
    else:
        return f'Наибольшая цифра {c}'
print (max_element(a))

