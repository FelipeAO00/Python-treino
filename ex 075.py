"""Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares."""

num = (
    int(input("Digite um numero: ")),
    int(input("Digite outro numero: ")),
    int(input("Digite mais um numero: ")),
    int(input("Digite o ultimo numero: "))
    )
print(f"A tupla ficou assim: {num}")

print(f"O numero 9 aparece um total de {num.count(9)} vezes")
if 3 in num:
    print(f"O numero 3 aparece na posicao {num.index(3)}")
else:
    print("O numero 3 nao aparece")

print("Os valores pares digitados foram:", end="")

for s in num:
    if s % 2 == 0:
        print({s}, end=" " )
