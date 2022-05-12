import math
a = float(input())
b = float(input())
c = float(input())
x1 = 0
x2 = 0
D = b**2 - (4*a*c)
if D > 0:
    x1 = -b + math.sqrt(D) / (2*a)
    x2 = -b - math.sqrt(D) / (2*a)
    print("Есть два корня " +x1 + x2)
elif D == 0:
    x1 = -b / (2*a)
    print("Есть один корень " + x1)
else:
    print("Нет корней")
