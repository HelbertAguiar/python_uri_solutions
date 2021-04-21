lista = input().split()
lista = list(map(lambda x: int(x), lista))
lista_sort = lista.copy()
lista_sort.sort()

for element in lista_sort:
    print(element)

print('')
for element in lista:
    print(element)