# Crie um programa que faça o computador jogar Jokenpô com você. (PEDRA PAPEL e TESOURA)

import random

print('{:=^40}'.format(' PEDRA PAPEL TESOURA '))

itens = ('Pedra', 'Papel','Tesoura')
opComp = random.randint(0,2)

print(
'''
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
''')

player = int(input('Qual a sua jogada ? '))

print('=' * 25)
print('Computador jogou: {}'.format(itens[opComp]))
print('Player jogou: {}'.format(itens[player]))
print('=' * 25)

if opComp == 0:
    if player == 0:
        print('EMPATE')
    elif player == 1:
        print('Player venceu !')
    elif player == 2:
        print('Computador Venceu !')
    else:
        print('Jogada Inválida !')

elif opComp == 1:
    if player == 0:
        print('Computador Venceu !')
    elif player == 1:
        print('EMPATE !')
    elif player == 2:
        print('Player venceu !')
    else:
        print('Jogada Inválida !')

elif opComp == 2:
    if player == 0:
        print('Player venceu !')
    elif player == 1:
        print('Computador Venceu !')
    elif player == 2:
        print('EMPATE !')
    else:
        print('Jogada Inválida !')
        