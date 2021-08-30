'''Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

– O primeiro valor é maior

– O segundo valor é maior

– Não existe valor maior, os dois são iguais'''

v1 = int(input('Digite o valor V1: '))
v2 = int(input('Digite o valor V2: '))

if v1 > v2:
    print('O valor V1 é maior que o valor V2')
elif v2 > v1:
    print('O valor V2 é maior que o valor V1')
else:
    print('Os valores são iguais')
