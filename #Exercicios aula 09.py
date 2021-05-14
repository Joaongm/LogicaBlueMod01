#Exercicios aula 09
'''
n=int(input('Digite o valor para consulta: '))


for cont in range(0,11):
    resultado = n*cont
    print('%d x %d = %d' %(n, cont, resultado) )


print()
Elaborar um programa para imprimir os números de 1 (inclusive) até 10 (inclusive) em ordem decrescente. '''
'''
print('inicio')
for cont in range(10,0,-1):
    print(cont)

'''
'''3. Faça um programa que leia o estado civil de 15 pessoas (Solteiro / Casado) e mostre ao final a quantidade de pessoas de cada estado civil. '''
'''
casadas=0
solteiras=0
var=3
for x in range(var):
    entrada=input('Informe o estado Civil(C = casado / S = Solteiro): ')
    if entrada in 'Cc':
        casadas +=1
    elif entrada in 'Ss':
        solteiras +=1
    else:
        print('Entrada invalida.')
        
  
print('%d Pessoas casadas e %d pessoas solteiras'%(casadas,solteiras))

'''

'''Faça um algoritmo que imprima 10 vezes a frase: “Go Blue”. 

'''
'''
print('Ínicio')
blue='Go Blue!'
for var in range(10):
    print(blue)

    '''

'''Faça um programa que mostre os valores numéricos inteiros ímpares situados na faixa de 0 a 20. '''

'''
print('Ínicio')
for cont in range(1,20,2):
    print(cont)
'''
'''
print('Panificadora Pão de Ontem')
price=float(input('Informe o preço do pão:'))
print()
for cont in range(1,51):
    total=price*cont
    print('{} - R$ {:.2f}'.format(cont, total))

'''    

'''
#exercício 08#
print('RESPONDA APENAS COM "SIM" OU "NÃO":')
positivas=0
negativas=0
respostas=[]
pergunta1=input('Telefonou para a vítima?')
respostas.append(pergunta1)
pergunta2=input('Esteve no local do crime?')
respostas.append(pergunta2)
pergunta3=input('Mora perto da vítima?')
respostas.append(pergunta3)
pergunta4=input('Devia para a vítima?')
respostas.append(pergunta4)
pergunta5=input('Já trabalhou com a vítima?')
respostas.append(pergunta5)
print(respostas)
for entrada in respostas:
    if entrada in 'Ss':
        positivas +=1
    elif entrada in 'Nn':
        negativas +=1
if positivas ==2:
    print('SUSPEITO')
elif positivas ==4 or positivas==3:
    print('CÚMPLICE')
elif positivas ==5:
    print('ASSASSINO')
else:
    print('INOCENTE')

print('FIM DO PROGRAMA')


'''

''' palpites da mega-sena:'''
'''
print('Possibilidades:')
palpites=0
for dezena1 in range(1, 61):
    for dezena2 in range(dezena1+1,61):
        for dezena3 in range(dezena2+1,61):
            for dezena4 in range(dezena3+1,61):
                for dezena5 in range(dezena4+1, 61):
                    for dezena6 in range(dezena5+1, 61):
                        palpites +=1
print(palpites)
   

'''
'''
#DESAFIO01
print('Ínicio do programa')
def func(valor):
    metade1 = valor//100
    metade2 = valor%100
    soma = metade1+metade2
    if soma**2 == valor:
        return valor
    else:
        return 'false'

for cont in range(1000,10000,1):
    if func(cont) != 'false':
        print(cont)
    # ou #

    for i in range(32, 100):
    dezena2 = (i*i)%100
    dezena1 = int(i*i/100)
    if dezena1+dezena2 == i:
        print(f'{i}^2 = {i*i}')
'''
'''

materias=int(input('Quantidade de matérias:'))
notas=[]

for cont in range(materias):
    nota=float(input(f'Qual sua nota na matéria {cont+1}?'))
    notas.append(nota)

print(f'{(sum(notas)/materias):.2f}')
'''