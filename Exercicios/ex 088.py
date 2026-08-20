"""
Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números 
entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
"""

from random import sample
from time import sleep

def main():

    print("="*20,"MEGA SENA","="*20)
    print()
    n_jogos = int(input("Digite o numero de jogos a serem feitos: "))
    print("-=" *40)
    jogos = []

    for _ in range(1, n_jogos + 1):

        lista_mega = sample(range(1, 61), 6)

        jogos.append(lista_mega)

        print(f"Jogo {_}: {lista_mega}")    
        sleep(0.1)

    print("-=" *40)
    print(30*" ","Fim da simulação.")
    print("-=" *40)

main()