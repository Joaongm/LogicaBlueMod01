#Inicio da aula#
#Um laço <for> é uma estrutura de repetição. Um loop.
#É um comando que faz a leitura de um objeto, percorrendo todos os seus elementos e toma ações dependendo de outros comandos que tenham sido atríbuidos a este laço.
# 
# 

from typing import Tuple


frase = 'Algo a se dizer sobre isso:'
for letra in frase:
    print(letra,end='..') 

for cont in range (1, 11):
    print(cont)

for cont in range (1, 41, 3):# de 1 até 40, de 3 em 3.
    print(cont)
print('============')
for cont in range (10, -1, -1):
    print(cont)
print('============')
for cont in range (0, 40, 2):
    print(cont)