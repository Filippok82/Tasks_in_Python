# 6. Выяснить является ли число чётным
# a=int(input('Ввведите число от 1 : '))

# if a%2==0:
#     print(f'число {a} четное')
# else:
#     print (f'число {a} нечетное')

a=int(input('Ввведите число:' ))
def isEven(a):
    if a % 2 == 0:
        return 'Четное'
    else:
        return 'Нечетное'
print(isEven(a))



