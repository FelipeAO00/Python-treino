#Exercício Python #061 - Progressão Aritmética v2.0
# Exercício Python 061: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.
"""
EX 51
print('PROGRESSAO ARITIMETICA 10 NUMEROS')

termo=int(input('Digite o primeiro termo da PA '))

razao=int(input('Digite a razao da PA '))

quantidade_termos = razao*10

for c in range(termo, quantidade_termos , razao):
    print(c)
"""
qt = 1
print("=" * 10,"Gerador de P.A", "=" *10)
termo = int(input("Digite o primeiro termo da P.A: "))
razao = int(input("Digite a razao da P.A: "))
for q in range(10):
    print(termo, end=" --> ",)
    termo += razao
    qt += 1
print("FIM.")