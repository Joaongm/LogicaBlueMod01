# O usuário deve digitar dois valores e o programa deve identificar se os valores são iguais ou diferentes#

def compare(a, b):
    if (a==b):
        print('Os números são iguais')
    else:
        print('Os números são diferentes')


n1 = int(input('Digite um número:'))
n2 = int(input('Digite outro número:'))

compare(n1, n2)
