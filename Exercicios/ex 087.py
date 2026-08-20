"""
Exercício Python 087: Aprimore o desafio anterior, mostrando no final: 
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
"""
lista = [[],[],[]]
try:
    for l in range(0,3):# para cadal linha
        for d in range(0,3): #uma coluna
            lista[l].append(int(input(f"Digite um numero [{l} , {d}]: ")))

except ValueError:
    print("Erro no codigo! Digite novamente ")
    print()



for l in range(0,3): # para cadal linha
    for d in range(0,3): #uma coluna 
        print(f"[{lista[l][d]:^5}]" , end="")        
    print()     

soma_par = []
for linha in lista:
    for numero in linha:
        if numero % 2 == 0:
            soma_par.append(numero)

soma_coluna3 = 0
for coluna in lista:
        soma_coluna3 += coluna[2]

maior_segunda_linha = max(lista[1])
        

#print(soma_coluna3)
print(f"A soma de todos os valores pares digitados são {sum(soma_par)}")
print(f"A soma dos valores da terceira coluna é {soma_coluna3}")
print(f"A O maior valor da segunda linha é {maior_segunda_linha}")


