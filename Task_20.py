# 20. Задать номер четверти, показать диапазоны для возможных координат
a=int(input('Введите номер четверти:'))
def quarter(a):
    if a==1:
        return 'x(0,n) y(0,n)'
    elif a==2:
        return 'x(0,-n) y(0,n)'
    elif a==3:
        return 'x(0,-n) y(0,-n)'
    elif a==4:
        return 'x(0,n) y(0,-n)'
print(quarter(a))