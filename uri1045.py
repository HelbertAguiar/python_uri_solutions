def forma_triangulo(a, b, c):
    if (a >= b + c): 
        print('NAO FORMA TRIANGULO')
        return
    if (a*a == (b*b) + (c*c)): print('TRIANGULO RETANGULO')
    if (a*a > (b*b) + (c*c)): print('TRIANGULO OBTUSANGULO')
    if (a*a < (b*b + c*c)): print('TRIANGULO ACUTANGULO')
    
    if (a == b) and ( b == c): print('TRIANGULO EQUILATERO')
    elif (a == b): print('TRIANGULO ISOSCELES')
    elif (b == c): print('TRIANGULO ISOSCELES')
    elif (c == a): print('TRIANGULO ISOSCELES')

lista = input().split()
lista = list(map(lambda x: float(x), lista))
lista.sort(reverse=True)

a = float(lista[0])
b = float(lista[1])
c = float(lista[2])

forma_triangulo(a, b, c)
