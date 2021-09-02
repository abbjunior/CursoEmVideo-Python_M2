'''
041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
 e mostre sua categoria, de acordo com a idade:

– Até 9 anos: MIRIM

– Até 14 anos: INFANTIL

– Até 19 anos: JÚNIOR

– Até 25 anos: SÊNIOR

– Acima de 25 anos: MASTER
'''
from datetime import date

anoAtual = date.today().year

anoAtleta = int(input('Digite seu ano de nascimento: '))

idade = anoAtual - anoAtleta

if idade <= 9:
    print('Atletas de {} anos São da categoria MIRIM'.format(idade))
elif idade <= 14:
    print('Atletas de {} anos São da categoria INFANTIL'.format(idade))
elif idade <= 19:
    print('Atletas de {} anos São da categoria JÚNIOR'.format(idade))
elif idade <= 25:
    print('Atletas de {} anos São da categoria SÊNIOR'.format(idade))
else:
    print('Atletas de {} anos São da categoria MASTER'.format(idade))
