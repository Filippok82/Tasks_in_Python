# 19. Определить номер четверти плоскости, в которой находится точка с координатами Х и У, причем X ≠ 0 и Y ≠ 0

x=float(input('Ввведите координату для x:'))
y=float(input('Ввведите координату для y:'))

def quarter_number(x,y):
    if x>0 and y>0:
        return ' первая четверть'
    elif x<0 and y>0:
        return 'вторая четверть'
    elif x<0 and y<0:
        return 'третья четверть'
    elif x>0 and y<0:
        return 'четвертая четверть'
print(quarter_number(x, y))
    
    
