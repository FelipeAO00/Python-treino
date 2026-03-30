#Exercício Python 051: Desenvolva um programa que leia o primeiro termo e a
# razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
print('PROGRASSAO ARITIMETICA 10 NUMEROS')

termo=int(input('Digite o primeiro termo da PA '))

razao=int(input('Digite a razao da PA '))

quantidade_termos = razao*10

for c in range(termo, quantidade_termos , razao):
    print(c)