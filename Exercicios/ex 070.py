"""Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos. 
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato. """
total = 0
cont = 0
barato = 0
while True:
    print("-" *40)
    print("           LOJA SUPER BARÃO")
    print("-" *40)
    product = str(input("Nome do produto: "))
    preço = int(input("Digite o preço do produto: R$"))
    total += preço
    if preço > 1000:
        cont += 1
    if barato == 0 or preço < barato:
        barato = preço
        beneficio = product
    next = str(input("Deseja continuar? [S/N] ")).lower().strip()
    if next == "n":
        break
print(f"O total da sua compra foi {total}")
print(f"Temos {cont} produtos custando mais de R$1000.00")
print(f"O produto mais barato foi {beneficio} que custa {barato}")