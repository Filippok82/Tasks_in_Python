# 8. Показать четные числа от 1 до N
# n = 1
# while n <= 10:       # четные числа без метода
#      if n % 2 == 0:
#          print(n)
#      n += 1

# __________________________________________________________________________
# def chet(n):
#     return list(range(0, n+1, 2)) # показать четные числа в списке методом используя шаги в range

# print(chet(10))

# n = int(input('Введите n: '))  

def chet(n):
    for i in range(1, n+1):
        if i%2==0:
            print(i)
    return i
print(chet(10))            
