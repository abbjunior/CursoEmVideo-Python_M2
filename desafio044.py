'''
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal 
e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço normal 

– 3x ou mais no cartão: 20% de juros
'''

produto = float(input('Digite o valor do produto: (R$) '))

print(('=') * 75)
print('Digite 1 para pagamento à vista em dinheiro ou cheque. 10% de desconto')
print('Digite 2 para pagamento à vista no cartão. 5% de desconto')
print('Digite 3 para pagamento até 2x. Preço normal')
print('Digite 4 para pagamento 3x ou mais. 20% de juros')
print(('=') * 75)

Fpag = int(input('Digite a forma de pagamento: '))

op1 = (produto - (produto * 0.10))
op2 = (produto - (produto * 0.05))
op4 = ((produto * 0.20) + produto)

if Fpag == 1:
    print('Seu produto custa: R$ {:.2f} Com desconto {:.2f}'.format(produto,op1))
elif Fpag == 2:
    print('Seu produto custa: R$ {:.2f} Com desconto {:.2f}'.format(produto,op2))
elif Fpag == 3:
    print('Seu produto custa: R$ {:.2f} Podendo pagar em 2X de R$ {:.2f}'.format(produto,produto / 2))
elif Fpag == 4:
    parcelas = float(input('digite o número de parcelas: 1 à 12 '))
    print('Seu produto custa: R$ {:.2f} Com juros {:.2f} Podendo pagar em {:.0f} vezes de R$ {:.2f}'.format(produto,op4,parcelas,op4 / parcelas))
else:
    print('OPÇÃO INVÁLIDA !')
    