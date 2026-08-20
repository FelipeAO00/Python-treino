"""
Exercício Python 091: 
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário em Python. 
No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
"""

def main():
    from time import sleep
    from random import randint
    from operator import itemgetter
    dicionario = dict()
    
    #d4 / d6 / d8 / d10 / d12 / d20

    while True:
        try:    
            dice_type = int(input("Digite o numero de um dos tipos de dados: d[4/6/8/10/12/20]: "))
            print()

            if dice_type not in [4, 6, 8, 10, 12, 20]:
                print("Valor de dado INVALIDO!, Valores validos -> d[4/6/8/10/12/20]: ")
                print()

            else:
                break
            
        except ValueError:
            print("Valor de dado INVALIDO!, Valores validos -> d[4/6/8/10/12/20]: ")


    dicionario["jogador_1"] = randint(1,dice_type)
    dicionario["jogador_2"] = randint(1,dice_type)
    dicionario["jogador_3"] = randint(1,dice_type)
    dicionario["jogador_4"] = randint(1,dice_type)

    print("Valores sorteados: ")
    print("=" *40)


    for jogador, valor in dicionario.items():
        print(f"{jogador} tirou {valor} no dado")
        sleep(1)

    print("=" *40)

    print("==Ranking dos jogadores==")

    ranking = sorted(dicionario.items(), key = itemgetter(1) , reverse = True)

    #print(ranking)
    print("=" *40)
    
    for posicao, (jogador, valor) in enumerate(ranking, 1):
        print(f"{posicao}º lugar: {jogador} com {valor} pontos")
    

main()