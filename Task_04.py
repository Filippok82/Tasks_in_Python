## Найти максимальное из трех чисел
a,b,c = int(input('a:')),int(input('b:')), int(input('c:'))
if a>b and a>c:
    print(f'max-{a}') 
elif b>a and b>c: 
    print(f'max-{b}')
elif c>a and c>b:
     print(f'max-{c}')
   