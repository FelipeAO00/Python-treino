"""
Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. 
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. 
Ao final, mostre o conteúdo das três listas geradas.
"""
listaUm = []
listaP = []
listaI = []

while True:
    try:
        n = int(input("Digite um numero: "))
        listaUm.append(n)

        if n % 2 == 0:
            listaP.append(n)
            print("Adicionado a lista Par")

        else:
            listaI.append(n)
            print("Adicionado a lista Impar")

        resp = str(input("Quer continuar [S/N] ")).strip().lower()

        if resp not in ["n","s"]:
            print("Digite apenas [S/N]. Tente novamente!")
            print()

        elif resp == "n":
            break


    except ValueError:
        print("Algum valor invalido foi digitado. Tente novamente. ")
        print()


print(f"A lista Completa é {listaUm}")
print(f"A lista Par é {listaP}")
print(f"A lista Impar é {listaI}")