# task_3.py
# Даны координаты центра окружности x0, y0 и ее радиус r.
# Также, дана точка (x, y). Определите,
# лежит ли данная точка внутри окружности
X0 = float(input())
Y0 = float(input())
r = float(input())
x = float(input())
y = float(input())
if (x-X0)**2 + (y-Y0)**2 <= r**2:
    print("точка лежит в окружности")
else:
    print("точка не лежит в окружности")
