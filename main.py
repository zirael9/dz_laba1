a = float(input("коэффициент a= "))
b = float(input("коэффициент b= "))
c = float(input("коэффициент c= "))
D = (b**2-4*a*c)
if a == 0:
    print("уравнение не является квадратным")
else:
    if D < 0:
        print("уравнение не имеет корней")
    else:
        print(((-b + D ** 0.5) / (2 * a)), ((-b - D ** 0.5) / (2 * a)))

