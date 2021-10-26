''' Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.'''

opcao = 0

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

while opcao != 5:
    opcao = int(input('''
        [ 1 ] somar
        [ 2 ] multiplicar
        [ 3 ] maior
        [ 4 ] novos números
        [ 5 ] sair do programa
    '''))
    if opcao == 1:
        soma = n1 + n2
        print('{} + {} = {} '.format(n1,n2,soma))
    elif opcao == 2:
        multiplica = n1 + n2
        print('{} x {} = {}'.format(n1,n2,multiplica))
    elif opcao == 3:
        if n1 == n2:
            print('Os número são iguais')
        elif n1 > n2:
            print('N1 = {} é maior'.format(n1))
        else:
            print('N2 = {} é maior'.format(n2))
    elif opcao == 4:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
    elif opcao == 5:
        print('FIM DO PROGRAMA !')
    else:
        print('OPÇÃO INVÁLIDA ! TENTE NOVAMENTE !')
