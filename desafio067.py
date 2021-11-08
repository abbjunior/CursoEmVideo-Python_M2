# Faça um programa que mostre a tabuada de vários números, um de cada vez, 
# para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for 
# negativo.

while True:
    n = int(input("Digite o número que deseja ver a tabuada: [0 PARA SAIR] "))
    if n <= 0:
        print('FIM DO PROGRAMA !')
        break
    else:
        for num in range (1,11):
            print(f'{num} x {n} = {num*n}')
