# Faça um programa que jogue par ou ímpar com o computador. 
# O jogo só será interrompido quando o jogador perder, 
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

print('-=' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-=' * 20)

v = 0

while True:
    jogador = int(input('Digite um valor: '))
    pc = randint(0, 10)
    total = pc + jogador
    opcao = ' '

    while opcao not in 'PI':
        opcao = str(input('Você quer par ou ímpar? (P/I) ')).upper().strip()[0]

    print(f'Você jogou {jogador} e o computador jogou {pc}. Total deu {total}.', end=' ')
    print('DEU PAR.' if total % 2 == 0 else 'DEU ÍMPAR.')

    if opcao in 'P':
        if total % 2 == 0:
            print('VOCÊ GANHOU! Vamos continuar...')
            v += 1
        else:
            print('Você perdeu!')
            break
    if opcao in 'I':
        if total % 2 == 1:
            print('VOCÊ GANHOU! Vamos continuar...')
            v += 1
        else:
            print('Você perdeu !')
            break
print(f'Fim do jogo ! Você venceu {v} vezes')
