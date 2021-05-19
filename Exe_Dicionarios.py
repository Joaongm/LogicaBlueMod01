'''
# Exercício Treino - Crie um dicionário em que suas chaves serão os números 1, 4, 5, 6, 7, e 9 (que podem ser armazenados em uma lista) e seus valores correspondentes aos quadrados desses números.​
#{1: 1, 4: 16, 5: 25, 6: 36, 7: 49, 9: 81}  ​

lista_nums = [(1,1**2) ,(4,4**2), (5, 5**2), (6,6**2), (7,7**2), (9,9**2)]

nums = dict(lista_nums)
print(nums)
# OU #
'''
'''
l1 = [1,4,5,6,7,9]
l2 = []

for cont in l1:
    l2.append(cont**2)

dic = dict(zip(l1,l2))
print(dic)

# OU #

quadrados = {}
for i in range(1, 11):
    quadrados [i] = (i**2)
for key, value in quadrados.items():
    print(f'{key} : {value}')


'''
#Exercício Treino - Crie um dicionário em que suas chaves correspondem a números inteiros entre [1, 10] e cada valor associado é o número ao quadrado.​
#{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100} 

'''
numslista = [(1,1**2),(2,2**2),(3,3**2),(4,4**2),(5,5**2),(6,6**2),(7,7**2),(8,8**2),(9,9**2),(10,10**2)]

numsdict = dict(numslista)
print(numsdict)
'''
'''
l1=[]
l2=[]
for cont in range(1,11):
    l1.append(cont)
    l2.append(cont**2)

dic =dict(zip(l1,l2))
print(dic)
'''
#Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo sa estrutura na tela. A média para aprovação é 7. Se o aluno tirar entre 5 e 6.9 está de recuperação, caso contrário é reprovado.

'''
print('Inclusão das médias')
print()
medias=[]
alunos = dict(medias)
qtdalunos= int(input('Quantos alunos(as) na turma?'))
for cont in range (qtdalunos):
    a = input('Digite o nome:')
    b = float(input('Digite a média:'))
    if b < 7 and b >= 5:
        situ = 'Em recuperação'
    elif b >= 7:
        situ = 'Aprovado'
    else:
        situ = 'Reprovado'
    medias.append(a)
    b = situ
    alunos[a]=b
print(alunos)       
'''


'''
Crie um programa em que 4 jogadores, joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário. No final coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado. Dicas: procure sobre a função randint(), sleep() e itemgetter da bliblioteca operator.
'''

from time import sleep
from operator import itemgetter
from random import randint
resultados=[]
jogadores =[]

for cont in range(4):
    nome=input('Nome do jogador:')
    sleep(.2)
    jogadores.append(nome)

for k in jogadores:
    result=randint(1, 6)
    resultados.append(result)
    print(f'O jogador {k} tirou {result} no dado')
    sleep(1)
dic = dict(zip(jogadores,resultados ))
resultados.sort(reverse=True)
dic=sorted(dic.items(), key=itemgetter(1), reverse=True)
nomeganhador=(dic[0][0])
resultadoganhador=(dic[0][1])
print('-'*10,'Resultado','-'*10)
print('O jogador vencedor foi o {} com o numero {}'.format(nomeganhador, resultadoganhador))

'''
#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário. Se por acaso a CTPS for diferente de 0, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente , além da idade , com quantos anos a pessoa vai se aposentar. Considere que o trabalhador deve contribuir por 35 anos para se aposentar.​​

'''