# ⦁	Crie um programa, utilizando dicionário, que simule a baixa de estoque das vendas de um supermercado. Não esqueça de fazer as seguintes validações:
#Produto Indisponível
#Produto Inválido
#Quantidade solicitada não disponível 
#O programa deverá mostrar para o cliente a quantidade de itens comprados e o total.


estoque = { 'ABACATE': [100, 4.50],
            'CENOURA': [50, 0.8],
            'ABÓBORA': [200, 1.4]}
opc = 1
totalprodutos=0
totalvalor=0
while opc==1:
    produto=input('Qual produto deseja?').upper()
    if produto in estoque:
        print('in estoque')
        preço= estoque[produto][1]
        
        qtd=int(input('Quantas unidades deseja?'))
        valor=qtd*preço
        if estoque[produto][0] < qtd:
            print('Quantidade indisponivel')
        else:
            print(qtd, 'x', produto,'=', valor)
        
        estoque[produto][0]-=qtd
        totalprodutos+=qtd
        totalvalor+=valor
    else:
        print('Não cadastrado')
    
    if input('Deseja continuar as compras? S/N') in 'Nn':
        opc=0
    else:
        opc=1

print('Você comprou ', totalprodutos, 'produtos, pelo valor total de R$:', totalvalor)