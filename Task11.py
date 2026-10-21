import math
# Считываем два радиуса из отдельных строк
radius1 = float(input())
radius2 = float(input())
# Определяем, какой из них внешний (больший), а какой внутренний (меньший)
R = max(radius1, radius2)
r = min(radius1, radius2)
# Вычисляем площадь кольца
area = math.pi * (R**2 - r**2)
# Выводим результат
print(area)