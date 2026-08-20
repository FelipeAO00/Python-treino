"""
Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e 
cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. 
No final, mostre os valores pares e ímpares em ordem crescente.
"""

lista_par = []
lista_impar = []

for val in range(1,8): 
    
    try:
        num = int(input(f"Digite o {val}º valor: "))
    
        if num % 2 == 0:
            lista_par.append(num)

        else:
            lista_impar.append(num)

    except ValueError:
            print("Erro de codigo!")
            print()
            
    
lista_geral = (lista_par, lista_impar)

print(f"Pares: {sorted(lista_geral[0])}")
print(f"Impares: {sorted(lista_geral[1])}")
print()
