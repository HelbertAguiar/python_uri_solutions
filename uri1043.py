def condicao_existencia_triangulo(a, b, c):
    status = False
    ladoA = False
    ladoB = False
    ladoC = False
    
    if (a > abs(b-c)) and (a < abs(b+c)):
        ladoA = True
    if (b > abs(a-c)) and (b < abs(a+c)):
        ladoB = True
    if (c > abs(b-a)) and (c < abs(b+a)):
        ladoC = True
    if (ladoA == True) and (ladoB == True) and (ladoC == True):
        status = True 

    return status

a, b, c = input().split()

a = float(a)
b = float(b)
c = float(c)

if condicao_existencia_triangulo(a, b, c) == True:
    perimetro = a + b + c
    print('Perimetro = %.1f' %float(perimetro))
else:
    area = ((a + b)*c)/2
    print('Area = %.1f' %float(area))