'''Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:
à vista dinheiro/cheque: 10% de desconto
à vista no cartão: 5% de desconto
em até 2x no cartão: preço formal
3x ou mais no cartão: 20% de juros'''

print('===== Supermecado Felipe =====')

valor=int(input('Preco das compras: '))
n=int(input('Insira a forma de pagamento: \n [1] A dinheiro/Pix \n [2] A vista cartao \n [3] 2x Cartao \n [4] 3x ou mais cartao \n Digite: '))
desconto = valor / 100 * 10
desconto2 = valor / 100 * 5
juros = valor * 20 / 100

if n==1:
    print(f'Sua compra de {valor} vai custar {valor - desconto :.1f} no final')

if n==2:
    print(f'Sua compra de {valor} vai custar {valor - desconto2 :.1f} no final')

if n==3:
    print(f'Sua compra de {valor} vai custar {valor} no final')

if n==4:
    parcelas=int(input('Quantas parcelas? '))
    tparcelas = valor / parcelas
    print(f'Sua compra de {valor} vai custar {valor + juros} \n Esta dividido em x{parcelas} de {tparcelas} com JUROS')
else:
    print('Forma de pagamento invalida!')



'''print('Sua compra de {valor} vai custar {} no final')'''