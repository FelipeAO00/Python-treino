#Exercício Python 055: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.



for p in range(1,6):
    peso = float(input(f"Peso da pessoa {p}: "))
    if p == 1:
        maior = peso
        menor = peso
    if peso > maior:
        maior = peso
    if peso <  menor:
        menor = peso
    
   

print(f"O maior peso lido foi {maior} e o menor peso lido foi {menor}")