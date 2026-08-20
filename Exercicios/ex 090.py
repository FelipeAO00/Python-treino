"""
Exercício Python 090: Faça um programa que leia nome e média de um aluno, 
guardando também a situação em um dicionário. 
No final, mostre o conteúdo da estrutura na tela.
"""

dicionario = dict()

dicionario['nome'] = str(input("Digite o nome do aluno: "))
dicionario['nota1'] = float(input("Digite a primeira nota do aluno: "))
dicionario['nota2'] = float(input("Digite a segunda nota do aluno: "))


dicionario['media'] = (dicionario["nota1"] + dicionario["nota2"]) / 2

if dicionario['media'] >= 7:
    dicionario['situação'] = "aprovado"

elif dicionario['media'] >= 6:
    dicionario['situação'] = "recuperação"

else:
    dicionario['situação'] = "reprovado"

print(f"Nome é igual a {dicionario['nome']}")
print(f"Notas é igual a, nota 1:[{dicionario['nota1']}] nota 2:[{dicionario['nota2']}]")
print(f"Media é igual a {dicionario['media']}")
print(f"Situação é igual a {dicionario['situação'].upper()}!")