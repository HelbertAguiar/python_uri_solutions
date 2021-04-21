import sys

n1, n2, n3, n4 = input().split()

n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)

num = float((n1*2) + (n2*3) + (n3*4) + (n4*1))
den = float(2+3+4+1)  
media_ponderada = float(num) / float(den)

print('Media: %.1f' %media_ponderada)
if media_ponderada >= 7.0 : 
    print('Aluno aprovado.')
    sys.exit(0)
if media_ponderada  < 5.0 : 
    print('Aluno reprovado.')
    sys.exit(0)

nota_exame = float(input())
if (media_ponderada >= 5.0) and (media_ponderada <= 6.9) :
    print('Aluno em exame.')
    print('Nota do exame: %.1f' %nota_exame)
    media_ponderada_final = float((media_ponderada + nota_exame)/2)
    if media_ponderada_final >= 5.0 : print('Aluno aprovado.')
    if media_ponderada_final  < 5.0 : print('Aluno reprovado.')
    print('Media final: %.1f' %media_ponderada_final)