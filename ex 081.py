"""
Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
""" 
lista = []
cont = 0
while True:
    try:
        n = int(input("Digite um numero: "))
        lista.append(n)
        s = str(input("Deseja continuar? [S/N] ")).strip().lower()
    except ValueError:
        print("Oe I A Oe I A A Oei A A A")

    if s == "n":
        break

print(f"Total de numeros digitados {len(lista)}")

print(f"Numeros ordenados de forma decrescente na lista ---> {sorted(lista, reverse=True)}")

if 5 in lista:
    print("Numero 5 encontrado na lista ")

else:
    print("Numero 5 nao foi encontrado na lista ")

if len(lista) in lista:
    print(f"O numero {len(lista)} esta na lista! ")
else:
    print(f"O numero {len(lista)} NÃO esta na lista ")