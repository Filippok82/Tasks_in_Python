# 17. По двум заданным числам проверять является ли одно квадратом другого
a=int(input('первое число:'))
b=int(input('второе число:'))

def checking_number(a,b):
    return a==b**2 or b==a**2
print(checking_number(a, b))


