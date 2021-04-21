def calcula_horas(inicio, fim):
    if inicio < fim:
        delta_horas = fim - inicio
        print('O JOGO DUROU ', delta_horas,' HORA(S)', sep='')
    elif inicio == fim:
        print('O JOGO DUROU ', 24,' HORA(S)', sep='')
    elif inicio > fim:
        delta_horas = (24 - inicio) + fim
        print('O JOGO DUROU ', delta_horas,' HORA(S)', sep='')

hi, hf = input().split()

hi = int(hi)
hf = int(hf)

calcula_horas(hi, hf)