#lista de exercicios aula10#

'''1--Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo representando a sua altura em centímetros.  Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.
-'''
'''
n=0
maior=0.1
menor = 3.0
menoraluno = n
maioraluno = n
for cont in range(10):
    n=int(input('Qual o número do aluno?'))
    
    alt = float(input('Qual a altura?'))

    if alt > maior:
        maior = alt
    
    if alt < menor:
        menor = alt

   ''' 


'''2---'''

'''
opc= True
while opc == True:
    senha=input('Digite a senha: ')
    if senha == 'novas3nha':
        opc = False
        print('fim do programa')
    else:
        print('Tente novamente!')
'''

''' Exercício 3 - Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. 
'''
'''
candidatos = ['', '1-LULA', '2-BOZO', '3-MARINA', '4-DILMA', '5-BRANCO', '6-NULO']
print(candidatos)
lula=0
bozo=0
marina=0
dilma=0
branco=0
nulo=0
print('Digite 0 para encerrar a votação!')
opc=True
voto=0
while opc==True:
    voto=int(input('Qual o seu voto?'))
    if voto == 1:
        lula+= 1
    elif voto == 2:
        bozo += 1
    elif voto == 3:
        marina += 1
    elif voto == 4:
        dilma +=1
    elif voto == 5:
        branco += 1
    elif voto == 0:
        opc = False
    else:
        nulo += 1

total = bozo + dilma + lula + marina+ branco+ nulo

print(f'O número total de votos foi de {total} votos')
print(f'O total de votos para o candidato bozo foi de {bozo} votos')
print(f'O total de votos para a candidata Dilma foi de {dilma} votos')
print(f'O total de votos para a candidata Marina foi de {marina} votos')
print(f'O total de votos para o candidato Lula foi de {lula} votos')
print(f'O total de votos em branco foi de {branco} votos, representando {(branco/total)*100:.2f}% da votação total')
print(f'O total de votos nulos foi de {nulo} votos, representando {(nulo/total)*100:.2f}% da votação total')

'''

#