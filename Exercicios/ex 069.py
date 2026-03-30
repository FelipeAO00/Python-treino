"""
Exercício Python 069: Crie um programa que leia a idade e o sexo de várias pessoas. 
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. 
No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.
"""
cont_idade = 0
cont_homem = 0 
cont_mulher = 0
while True:
    print("-" *40)
    print("         Cadastre uma pessoa")
    print("-" *40)

    idade = int(input("Idade: "))
    if idade >= 18:
        cont_idade += 1
    sexo = str(input("Sexo: [M/F] ")).lower().strip()
    while sexo not in "mf":
        sexo = str(input(f"Sexo invalido. Digite novamente: [M/F]")).lower().strip()
    if sexo == "m":
        cont_homem += 1
    if sexo == "f" and idade < 20:
        cont_mulher += 1
    print("-" *40)
    next = str(input("Quer continuar? [S/N] ")).lower().strip()
    print("-" *40)
    if next == "n":
        break
print(f"Numero de pessoas com mais de 18 é {cont_idade}")
print(f"Total de homens cadastrados é {cont_homem}")
print(f"Total de mulheres com menos de 20 anos é {cont_mulher}")