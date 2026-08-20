"""
Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
"""

geral = list()
dados = list()

while True:
    try:
        dados.append(str(input("Digite um nome: ")).strip().title())
        dados.append(int(input("Digite o peso: ")))

        geral.append(dados[:])
        dados.clear()
        r = str(input("Quer continuar? [S/N]  ")).strip().lower()
        if r == "n":
            break
    
    except ValueError:
        print("Algum valor invalido foi digitado. Tente novamente. ")
        print()

menor = min(peso[1] for peso in geral)
maior = max(peso[1] for peso in geral)

print(f"Ao todo {len(geral)} pessoas foram cadastradas ")

print(f"As pessoas com menor peso registrado foram ", end="")
for peso in geral:
    if peso[1] == menor:
        print(peso[0],  end=" ")
print()

print(f"As pessoas com maior peso registrado foram ", end="")
for peso in geral:
    if peso[1] == maior:
        print(peso[0] , end=" ")
print()
