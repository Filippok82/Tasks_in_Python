# 14. Найти третью цифру числа или сообщить, что её нет


# a=int(input('Введите число: '))
# def three_element (a):
#     c=a%10
#     if a>=100 and a<1000:
#         return f'третья цифра числа: {c}'
#     else:
#         return 'третьей цифры в числе нет'
# print (three_element(a))


a=list(input('Введите число:'))

def three_element(a):
    b=len(a)
    if b<=2:
        return f'В числе только {b} цифры'
    else:
        return f'Третья цифра числа {a [2]}'
print(three_element(a))

