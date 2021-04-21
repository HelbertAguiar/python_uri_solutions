qtd_frutas, qtd_lista_nomes = (input()).split()
qtd_frutas = int(qtd_frutas)
qtd_lista_nomes = int(qtd_lista_nomes)

listafrutas = []
for i in range(qtd_frutas):
    listafrutas.append(input().lower())

listaNomes = []
for i in range(qtd_lista_nomes):
    listaNomes.append(input().lower())

for fruta in listafrutas:
    encontrouFruta = False
    for nome in listaNomes:
        if (nome.find(fruta) >= 0) or nome.find(fruta[::-1]) >= 0:
            encontrouFruta = True 
            break
    
    if encontrouFruta == True:
        print('Sheldon come a fruta ', fruta, sep='')
    elif encontrouFruta == False:
        print('Sheldon detesta a fruta ', fruta, sep='')
    