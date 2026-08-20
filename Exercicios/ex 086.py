"""
Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3x3 e 
preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.
"""
matriz = []

for linha in range(3):
    linha_atual = []

    for coluna in range(3):
        valor = int(input(f"Digite um valor para [{linha}, {coluna}]: "))
        linha_atual.append(valor)

    matriz.append(linha_atual)

print("-=" * 20)

for linha in matriz:
    print(linha, end="")
    print()