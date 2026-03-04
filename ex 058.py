#Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.
import random
resposta = 0
numero = random.randint(1,100)
temp = 0
cont = 0


print("um numero foi sorteado de 1 a 100, consegue advinhar qual é?: ")
while resposta is not numero:
   
            

    resposta = int(input("Digite um numero: "))
    cont += 1

    if resposta < 1 or resposta > 100:
        print("O numero esta entre 1 a 100")
    

    if resposta > numero:
        print(f"o numero e menor que {resposta}")
        

    elif resposta < numero:
        print(f"o numero e maior que {resposta}")

    else:
        print(f"parabens o numero é {numero}")


print(f"Voce levou {cont} tentativa(s)")
