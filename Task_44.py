# 44. Найти точку пересечения двух прямых заданных уравнением y = k1 * x + b1, y = k2 * x + b2, b1 k1 и b2 и k2 заданы
import sympy as sym

k1 = int(input('k1= '))
k2 = int(input('k2= '))
b1 = int(input('b1= '))
b2 = int(input('b2= '))

x = sym.Symbol('x')
y = sym.Symbol('y')

x = sym.solve((k1 * x + b1)-(k2 * x + b2))
print(x)

x1=int(input('подставим в формулу значение Х = '))

y = k1 * x1 + b1
sym.factor(y)
print(f'точка пересечения имеет координаты ({x1},{y})')