# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
# No final do programa, mostre: a média de idade do grupo, 
# qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

somaIdade = 0
mediaIdade = 0
maiorIdadeHomem = 0
nomeVelho = ''
totalMulher20 = 0

for pessoa in range (1, 5):
    print('=== {}ª Pessoa ==='.format(pessoa))
    nomePessoa = str(input('Digite o nome: ')).strip()
    idadePessoa = int(input('Digite a idade: '))
    sexoPessoa = str(input('Digite o Sexo (M/F): ')).strip()

    if pessoa == 1 and sexoPessoa in 'mM':
        maiorIdadeHomem = idadePessoa
        nomeVelho = nomePessoa
    if sexoPessoa in 'mM' and idadePessoa > maiorIdadeHomem:
        maiorIdadeHomem = idadePessoa
        nomeVelho = nomePessoa
    if sexoPessoa in 'fF' and idadePessoa < 20:
        totalMulher20 = totalMulher20 + 1

    somaIdade = somaIdade + idadePessoa

mediaIdade = somaIdade / 4

print('Média de idade do grupo: ', mediaIdade)
print('O homem mais velho tem {} anos e se chama {}'.format(maiorIdadeHomem,nomeVelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totalMulher20))
