#Exercício Python 056 - Analisador completo
somaidade = 0
nomevelho = ""
idadevelho = 0  
Num_mulher = 0
for n in range (1 , 5):
    print(f"----Pessoa {n}----")

    nome = str(input("Nome: "))
    
    idade = int(input("Idade: "))
    
    sexo = str(input("M/F: ")).strip().upper()

    somaidade += idade
    if n == 1 and sexo == "M":
        nomevelho = nome
        idadevelho = idade

    if sexo in "M" and idade > idadevelho:
        idadevelho = idade
        nomevelho = nome

    if sexo == "F" and idade < 20 :
        Num_mulher += 1

print(f"A media de idade do grupo e de {(somaidade / 4)} anos")
print(f"O homem mais velho do grupo tem {idadevelho} anos e se chama {nomevelho}")
print(f"Ao todo sao {Num_mulher} mulheres com menos de 20 anos ")