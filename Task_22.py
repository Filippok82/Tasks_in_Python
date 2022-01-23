# 22. Найти расстояние между точками в пространстве 2D/3D


import math
def distantion_2d(x1,y1,x2,y2):
    return math.sqrt(math.pow(x2-x1,2)+math.pow(y2-y1,2))
print(distantion_2d(0, 0, 2, 2))

def distantion_3d(x1,y1,z1,x2,y2,z2):
    return math.sqrt(math.pow(x2-x1,2)+math.pow(y2-y1,2)+ math.pow(z2-z1,2))
print(distantion_3d(0, 0, 0, 2, 2, 2))