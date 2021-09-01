'''Faça um programa que leia o ano de nascimento de um jovem e informe, 
de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, 
se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''

from datetime import date

anoAtual = date.today().year

anoNasc = int(input('digite seu ano de nascimento: '))

idade = anoAtual - anoNasc
tempoFalta = 18 - idade
tempoPassou = idade - 18

if idade == 18:
    print('Ano de se alistar !')
elif idade < 18:
    print('Ainda não está na hora de se alistar. Faltam {} anos'.format(tempoFalta))
elif idade > 18:
    print('Passou da hora de se alistar. Passaram {} anos'.format(tempoPassou))
