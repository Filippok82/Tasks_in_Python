#15. Дано число. Проверить кратно ли оно 7 и 23
# a = int(input('Введите число:' ))
# print (a % 7 == 0 and a % 23 == 0)

a=int(input('Введите число: '))
def multiple (a):
    if a%7==0 and a%23==0:
        return f'Число {a} кратно 7 и 23'
    else:
        return f'Число {a} не кратно 7 и 23'
print(multiple(a))