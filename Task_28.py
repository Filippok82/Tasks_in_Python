# 28. Подсчитать сумму цифр в числе
 
number=list(input('Введите число:'))

def sum_number(number):
    return sum(map(int, list(number)))
print (sum_number(number))

