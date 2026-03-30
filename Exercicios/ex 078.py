"""
Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. """

"""
list = [int(input("Digite um valor para a posicao 0: ")), int(input("Digite um valor para a posicao 1: ")), 
        int(input("Digite um valor para a posicao 2: ")), int(input("Digite um valor para a posicao 3: ")), 
        int(input("Digite um valor para a posicao 4: "))]
print(f"Voce digitou os valores, {list}")
print(f"O maior valor digitado foi {max(list)} que apareceu nas posições {list.index(max(list))}, {list.index(max(list))}")
print(f"O maior valor digitado foi {min(list)} que apareceu nas posições {list.index(min(list))}")
"""
listnum = []

maxnum = 0
minnum = 0

for num in range(0,5):
    listnum.append(int(input(f"Digite um valor para a posicao {num}: ")))
    if num == 0:
        maxnum = minnum = listnum[num]
    else:
        if listnum[num] > maxnum:
            maxnum = listnum[num]
        if listnum[num] < minnum:
            minnum = listnum[num]
        

print()

print(f"Os valores digitados foram {listnum}")

print()

print(f"O maior valor digitado foi {maxnum}, que apareceu nas posicoes: " , end="")

for pos, data in enumerate(listnum):
   if data == maxnum:
       print(f"{pos}..." , end= "" )

print()

print(f"O maior valor digitado foi {minnum}, que apareceu nas posicoes: " , end="")

for pos, data in enumerate(listnum):
   if data == minnum:
       print(f"{pos}..." , end= "" )
print()