#12. Удалить вторую цифру трёхзначного числа
# a=int(input('Введите трехзначное число: '))  # Решение без метода
# b = a // 100 * 10 + a % 10
# print(f'получилось: {b}')

def two_elememt(a):
    b = a//100*10+a%10
    return b
print(two_elememt(325))    
