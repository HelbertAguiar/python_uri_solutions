def processaDuracao(hi, mi, hf, mf):
    
    delta_hr = 0
    delta_min = 0

    if hf == hi and mf == mi:
        delta_hr = 24
        delta_min = 0
        print('O JOGO DUROU ', int(delta_hr), ' HORA(S) E ', int(delta_min), ' MINUTO(S)', sep='')

    if hf == hi and mf > mi:
        delta_hr = 0
        delta_min = mf - mi
        print('O JOGO DUROU ', int(delta_hr), ' HORA(S) E ', int(delta_min), ' MINUTO(S)', sep='')
    
    if hf == hi and mf < mi:
        delta_hr = 23
        delta_min = 60 - abs(mf - mi)
        print('O JOGO DUROU ', int(delta_hr), ' HORA(S) E ', int(delta_min), ' MINUTO(S)', sep='')

    if hf < hi and mf <= mi:
        delta_hr = 24 - abs(hf - hi) - 1
        delta_min = 60 - abs(mf - mi)
        if delta_min >= 60:
                delta_hr = delta_hr + 1
                delta_min = delta_min - 60
        print('O JOGO DUROU ', int(delta_hr), ' HORA(S) E ', int(delta_min), ' MINUTO(S)', sep='')
    
    if hf < hi and mf > mi:
        delta_hr = 24 - abs(hf - hi) - 1
        delta_min = mf + abs(60-mi)
        if delta_min >= 60:
            delta_hr = delta_hr + 1
            delta_min = delta_min - 60
        print('O JOGO DUROU ', int(delta_hr), ' HORA(S) E ', int(delta_min), ' MINUTO(S)', sep='')

    if hf > hi and mf <= mi:
        if hf == hi + 1:
            delta_hr = 0
            delta_min = mf + abs(60-mi)
            if delta_min >= 60:
                delta_hr = delta_hr + 1
                delta_min = delta_min - 60
            print('O JOGO DUROU ', int(delta_hr), ' HORA(S) E ', int(delta_min), ' MINUTO(S)', sep='')
        elif mf < mi:
            delta_hr = hf - hi - 1
            delta_min = mf + abs(60-mi)
            print(delta_min)
            if delta_min >= 60:
                delta_hr = delta_hr + 1
                delta_min = delta_min - 60
            print('O JOGO DUROU ', int(delta_hr), ' HORA(S) E ', int(delta_min), ' MINUTO(S)', sep='')
        elif mf == mi:
            delta_hr = hf - hi
            delta_min = 0
            print('O JOGO DUROU ', int(delta_hr), ' HORA(S) E ', int(delta_min), ' MINUTO(S)', sep='')

    if hf > hi and mf > mi:
        delta_hr = hf - hi
        delta_min = abs(mf-mi)
        if delta_min >= 60:
            delta_hr = delta_hr + 1
            delta_min = delta_min - 60
        print('O JOGO DUROU ', int(delta_hr), ' HORA(S) E ', int(delta_min), ' MINUTO(S)', sep='')
    
# entrada = str(input())
entrada = '10 12 12 12'

horaIni, minutoIni, horaFim, minutoFim = entrada.split(' ')
processaDuracao(int(horaIni), int(minutoIni), int(horaFim), int(minutoFim))