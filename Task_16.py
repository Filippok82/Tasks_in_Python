# 16. Дано число обозначающее день недели. Выяснить является номер дня недели выходным 

a=int(input('Введите число от 1 до 7:'))

def number_day(a):
    if a==6 or a==7:
        return 'Выходной'
    else:
        return 'Будни'
print(number_day(a))