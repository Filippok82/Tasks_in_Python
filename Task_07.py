# 7.Показать числа от -N до N

# n=int(input('Введите число n: '))
# ran=range(-n,n+1)
#
#     print(i)


n = int(input('Введите число n: '))


def elemets(n):
    for i in range(-n, n+1):
        print(i)
    return i
print(elemets(n))
