def busca_elemento(matrix, li, ci, qtd_col):
    index = (li*qtd_col) + ci
    return (matrix[index])

def imprime_matrix(matrix, lin, col):

    for i in range(lin):
        print('\n', end='')
        for j in range(col):
            print(matrix[(i*col) + j], end=' ')

    print('\n', end='')
    return

def convert_list_to_string(lista):
    txt = ""  
    for element in lista:  
        txt += element
    return txt

def percorre_diagonal(word, matrix, qtd_lin, qtd_col):
    
    diag_list = []
    contador_match = 0
    diag_string = ''

    col = 0
    for k in range(qtd_lin):
        # print('x = ', 19-k, '; y = ', col, sep='')
        new_x = 19-k
        new_y = col
        diag_list.append(busca_elemento(matrix, new_x, new_y, qtd_col))
        col+=1
    
    diag_string = convert_list_to_string(diag_list)
    # print(diag_string)

    if diag_string.find(word) >= 0 or diag_string.find(''.join(reversed(word))) >= 0:
            contador_match = contador_match + 1
            # print(diag_string, contador_match, sep=' / ocorrencia -> ')

    diag_list.clear()
    # print('\n')
    
    return contador_match

def percorre_diagonal_sup(word, matrix, qtd_lin, qtd_col):

    contador_match = 0
    diag_string = ''
    diag_list = []

    # print('')
    for k in range(qtd_lin-1):  
        # print(k, 0, end=' ==> ')

        for l in range(qtd_col):
            if (abs(l) < qtd_col):
                # print(-l, l, sep=' ', end=' // ')
                new_x = k + (-l)
                new_y = 0 + (l)
                if (new_x >= 0) and (new_y >=0):
                    # print(new_x, new_y, sep=' ', end=' // ')
                    diag_list.append(busca_elemento(matrix, new_x, new_y, qtd_col))

        # print(diag_list)
        diag_string = convert_list_to_string(diag_list)
        # print(diag_string)
        
        if diag_string.find(word) >= 0 or diag_string.find(''.join(reversed(word))) >= 0:
            contador_match = contador_match + 1
            # print(diag_string, contador_match, sep=' / ocorrencia -> ')

        diag_list.clear()
        # print('\n')
    
    return contador_match

def percorre_diagonal_inf(word, matrix, qtd_lin, qtd_col):

    contador_match = 0
    diag_string = ''
    diag_list = []

    # print('')
    for k in range(qtd_col):
        if k == 0: continue
        # print(19, k, end=' ==> ')
        for l in range(qtd_col-1):
            if (abs(l) < qtd_col):
                # print(-l, l, sep=' ', end=' // ')
                new_x = (qtd_col - 1) + (-l)
                new_y = k + (l)
                if (new_x < qtd_col) and (new_y < qtd_col):
                    # print(new_x, new_y, sep=' ', end=' // ')
                    diag_list.append(busca_elemento(matrix, new_x, new_y, qtd_col))
        # print('\n')

        # print(diag_list)
        diag_string = convert_list_to_string(diag_list)
        # print(diag_string)
        
        if diag_string.find(word) >= 0 or diag_string.find(''.join(reversed(word))) >= 0:
            contador_match = contador_match + 1
            # print(diag_string, contador_match, sep=' / ocorrencia -> ')

        diag_list.clear()
        # print('\n')
    
    return contador_match


# ======== Main ==========================================================

qtd_word, lin, col = input().split()

qtd_word = int(qtd_word)
lin = int(lin)
col = int(col)

# salva lista de palavras
lista_word = []
for i in range(qtd_word):
    lista_word.append(input().lower())

# salva matrix de palavras
matrix = []
for i in range(lin):
    txt = str(input().lower())
    for x in txt:
        matrix.append(x)
pass

# imprime matrix
# imprime_matrix(matrix, lin, col)

for word in lista_word:

    not_find = 0

    # if word != 'maturidade':
    #     continue

    matchs = 0 
    matchs = percorre_diagonal(word, matrix, lin, col)
    if matchs > 0:
        print('1 Palavra \"', word, '\" na diagonal secundaria', sep='')
    else:
        not_find+=1

    matchs = 0 
    matchs = percorre_diagonal_sup(word, matrix, lin, col)
    if matchs > 0:
        print('2 Palavra \"', word, '\" acima da diagonal secundaria', sep='')
    else:
        not_find+=1

    matchs = 0
    matchs = percorre_diagonal_inf(word, matrix, lin, col)
    if matchs > 0:
        print('3 Palavra \"', word, '\" abaixo da diagonal secundaria', sep='')
    else:
        not_find+=1
    
    if not_find == 3 :
        print('4 Palavra \"', word, '\" inexistente', sep='')