# alguns usos da condicional 'while'#

#opc=0






'''

'''
'''
for cont in range(1,60, 2):
    print(cont)'''
'''
cont = -1
while cont <58:
    cont+=1
    print(cont)'''


'''cont=0
while cont<60:
    if cont % 2 != 0:
        print(cont)
    cont +=1'''

##PROGRAMA CONTÍNUO:##
opc=1
while opc== 1:
    qtd = int(input('Digite a quantidade de numeros impares a serem mostrados:'))
    num = 1
    cont = 1
    números = []
    while cont <= qtd:
        print(num)
        números.append(num) 
        cont = cont + 1
        num = num + 2
        
    print()   
    print(len(números), 'Números ímpares')
    print('em lista: ', números)
    print()
    for i in números:
        revertido = sorted(números,reverse=True)
    for num in revertido:
        print(num)


    aux = len(números)

    for i in range(aux, 1,1):
        print(números[aux])
    resp = input('Deseja reiniciar o programa? (S/N):').upper()
    while resp != 'S' and resp != 'N':
        print('Comando inválido')
        resp= input('Deseja reiniciar o programa? (S/N):').upper()
    while resp == 'N':
        print('FIM DO PROGRAMA')
        opc = 0
        resp = ''
''''''