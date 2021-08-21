# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

Vcasa = float(input('Digite o valor da casa: R$ '))
salario = float(input('Digite seu salário: R$ '))
anos = int(input("Quantos anos de financiamento: "))

prestacao = Vcasa / (anos * 12)                 # Calculo das prestações
salario30por100 = salario * 0.30                # Calculo 30% do salário

if prestacao > salario30por100:
    print('Negado !')
else:
    print('Aprovado !')
    print('Valor do imóvel: R$ {:.2f}'.format(Vcasa))
    print('Total de parcelas: {}'.format(anos * 12))
    print('Valor das parcelas: R$ {:.2f}'.format(prestacao))
