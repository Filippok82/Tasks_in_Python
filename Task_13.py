#13. Выяснить, кратно ли число заданному, если нет, вывести остаток.

a=int(input('Введите число: '))

def multiple (b):
    c=b%a
    if c==0:
        return 'Число кратно заданому'
    else:
        return f'остаток {c}'
print(multiple(20))