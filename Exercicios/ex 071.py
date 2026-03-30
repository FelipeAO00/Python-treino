"""
Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. 
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) 
e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
"""
print("-" *40)
print("Banco MASTER") # {:^20}
print("-" *40)
saque = int(input("Qual valor deseja sacar? R$"))
print("-" *40)
total = saque
cont = 0
ced = 50
while True:
    if total >= ced:
        total -= ced
        cont += 1 
    else:
        if cont > 0:
            print(f"O total de ced é {cont} cedulas em R${ced}")
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        cont = 0
        if total == 0:
            break        