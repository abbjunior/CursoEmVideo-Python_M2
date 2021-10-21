# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. 
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram 
# necessários para vencer.

import random

palpites = 1
numero = 0

numero = random.randint(0,10)

print('JOGO DE ADIVINHAÇÃO')
print('')

numeroUser = int(input('Digite um número de 0 a 10: '))


while numero != numeroUser:
    palpites = palpites + 1
    print('Você errou, tente novamente !')
    if numero > numeroUser:
        print('Dica: O numero sorteado é maior')
    else:
        print('Dica: O numero sorteado é menor')
    print('')
    numeroUser = int(input('Digite um número de 0 a 10: '))

print('Parabéns ! Você acertou em {} palpites'.format(palpites))
print('O número sorteado foi {}'.format(numero))
