# Exercício Python #054 - Grupo da Maioridade

#Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
maiores = 0
menores = 0
ano = 2026
for p in range(1 , 8):
    

    nascimento = int(input(f"Em que ano pessoa {p} nasceu?: "))
    if nascimento == str:
        print("texto foi digitado, reinicie o codigo")

    if ano - nascimento >= 18:
        maiores += 1

    else:
        menores += 1

if maiores <=1:
    print(f"{maiores} pessoa e maior de idade")

elif maiores == 0:
    print("nenhuma pessoa e maior de idade")

else:
    print(f"{maiores} pessoas sao maiores de idade")

if menores <=1:
    print(f"{menores} pessoa e menor de idade")

elif menores == 0:
    print("nenhuma pessoa e menor de idade")

else:
    print(f"{menores} pessoas sao menores de idade")