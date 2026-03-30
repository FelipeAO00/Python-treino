#Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador. 
#O jogo só será interrompido quando o jogador perder, 
#mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
while True:
    print("=" * 40)
    print("Vamos jogar PAR OU IMPAR!")
    print("=" * 40)

    val_pc = randint(1,100)
    p_i = str(input("Par ou Impar? [P/I] ")).strip().lower()
    val = int(input("Digite um valor: "))
    total = val + val_pc
    resultado = val + val_pc
    if resultado %2 == 0:
        resultado = "par"
    else:
        resultado = "impar"
    print(f"Voce jogou {val}, e o computador jogou {val_pc}, o total deu {total}, que é {resultado} ")
    if p_i == "p":
        p_i = "par"
    else:
        p_i = "impar"
    if resultado == p_i:
        print("Voce venceu!")
        print("Vamos jogar novamente!")
    else:
        print("Voce perdeu, SEU OTARIO!")
        break