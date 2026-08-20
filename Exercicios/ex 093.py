"""Exercício Python 093: 
Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
O programa vai ler o nome do jogador e quantas partidas ele jogou. 
Depois vai ler a quantidade de gols feitos em cada partida. 
No final, tudo isso será guardado em um dicionário,
incluindo o total de gols feitos durante o campeonato."""

def main():
#================================================================================================================================================
    prancheta_jogador = dict()
    gols_dados = list()
    while True:
        try:
            print("Analise de Jogador")

            prancheta_jogador['nome_jogador'] = str(input("Digite o nome do jogador: ")).strip().title()
            prancheta_jogador['numero_partidas'] = int(input(f"Quantas partidas {prancheta_jogador['nome_jogador']} jogou? "))
            for pergunta_gols in range(1, prancheta_jogador['numero_partidas'] + 1):
                gols_dados.append(int(input(f"Quantos gols na partida {pergunta_gols}? ")))

            break

        except ValueError:
            print("Algum valor invalido foi digitado. Tente novamente. ")
            print()
#================================================================================================================================================
    print("-="*40)

    prancheta_jogador['gols_partida'] = gols_dados
    prancheta_jogador['total_gols'] = total = sum(gols_dados)
    print(prancheta_jogador)

#================================================================================================================================================
    print("-="*40)

    print(f"O nome do jogador é {prancheta_jogador['nome_jogador']} ")
    print(f"O total de partidas é {prancheta_jogador['numero_partidas']} ")
    print(f"O numero total de gols é {prancheta_jogador['total_gols']} ")

#================================================================================================================================================
    print("-="*40)

    print(f"O jogador {prancheta_jogador['nome_jogador']} jogou {prancheta_jogador['numero_partidas']} partidas")
    for partida in range(1, prancheta_jogador['numero_partidas'] + 1):
        print(f"=> Na partida {partida}, fez {prancheta_jogador['gols_partida'][partida - 1]} gols")
    print(f"{prancheta_jogador['nome_jogador']} fez um total de {prancheta_jogador['total_gols']}")

#================================================================================================================================================
main()