# 25. Найти сумму чисел от 1 до А
def sum (a):
    s=0
    for i in range(1,a+1):
        s+=i
    return s   
print(sum(25))