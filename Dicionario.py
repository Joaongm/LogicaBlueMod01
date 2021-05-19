# aula 011 #
''' Dicionário '''
'''
lista_contatos = [('Jojo','3388-9090'), ('Luana','9907-8464') , ('Niets','8257-9089'), ('Mark','9587-1313')]
print(lista_contatos[2][0])

# Para criar listas usamos []

# Para criar dicionários utiliza-se {} ou a função <dict>

contatos = dict(lista_contatos)

print (contatos['Niets'])


# método Get -> buscar valores em dicionários pela Key(chave)
notfoun = 'Contato não encontrado'

print(contatos.get('Loren', notfoun))
print(contatos.get('Luana', notfoun))

# método Values -> buscar valores em um dicionário(retorna True / False)

print('9587-1313' in contatos.values())

print('-='*50)
print('Adicionando contatos no dicionario')
print()
contatos ['Mulher Maravilha'] = '2233-9765'
contatos ['Deadpool'] = '666'
print(contatos)

# Adicionando Chaves e Valores com input(método 1):
'''

'''
a = input('Digite o nome:')
b = input('Digite o telefone:')
contatos[a]=b
print(contatos)
print()
'''
#Adicionando Chaves e Valores com input(método 2):
'''
contatos[input('Digite o nome:')] = input('Digite o telefone:')
print(contatos)

print()
print('-='*40)
print('Removendo contatos no dicionário:')

'''
'''
del contatos['Mulher Maravilha']
print(contatos)
print(contatos.pop('Deadpool', 'Não incluso'))
print(contatos)

print('=-'*40)
print('Unindo dicionários')
print()

contatos_niets = [('Jojoo','3388o-9090'), ('Luanoa','9907-846o4') , ('Nieots','8257-908o9'), ('Marok','9o587-1313')]
contatos2 = dict(contatos_niets)
for nome in contatos2:
    contatos[nome] = contatos2[nome]
    
print(contatos)
print()

# OU #
contatos.update(contatos_niets)


print(contatos)
print()
'''
#Exemplo 2 #





vingadores = {'Iron Man':'Robert Downey Jr.' , 'Captain America':'Chris Evans', 'Thor':'Chris Hemsworth', 'Black Widow':'Scarlett Johansson', 'Hulk':'Mark Ruffalo', 'Nick Fury':'Samuel L. Jackson', 'Vision':'Paul Bettany', 'Antman':'Paul Rudd', 'God':'Stan Lee'}

vingadores_lista = ['Miranha', 'Lóqui','Tânus','Bátima']


print(vingadores)

print('-='*40)
for k,v in vingadores.items():
    print(k,'-', v)

for i,v in enumerate (['Miranha', 'Lóqui','Tânus','Bátima']):
    print(i+101,'-',v)
