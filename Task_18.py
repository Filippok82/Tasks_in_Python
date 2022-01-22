# 18. Проверить истинность утверждения ¬(X ⋁ Y V Z) = ¬X ⋀ ¬Y Λ ¬­Z
def LogTask(x,y,z):
    return not(x or y or z) == (not x and y and z)  

for x in range(0,2):
    for y in range(0,2):
        for z in range(0,2):
          print (LogTask(x,y,z))  
    
