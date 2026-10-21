import math
a = float(input("Длина 1 стороны треугольника:"))
b = float(input("Длина 2 стороны треугольника:"))
c = float(input("Длина 3 стороны треугольника:"))
alpha = math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))
beta = math.degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c)))
gamma = math.degrees(math.acos((a**2 + b**2 - c**2) / (2 * a * b)))
print(alpha)
print(beta)
print(gamma)

