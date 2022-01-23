# 21.Программа проверяет пятизначное число на палиндромом.

number=str(input('Введите пятизначное число:'))

def polindrom(number):
    rebmun=number[::-1]
    if number==rebmun:
        return 'полиндром'
    else:
        return 'не полиндром'
print(polindrom(number))