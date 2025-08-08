'''Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você.'''
from random import randint

opcoes = 'Pedra' , 'Papel' , 'Tesoura'

computador = randint(0,2)

print('=== JO-KEN-PO ===')
print(""" 
[0] Pedra 
[1] Papel
[2] Tesoura 
""")
jogador=int(input('Selecione sua jogada: '))

print(f'O computador Jogou {(opcoes[computador])}')
print(f'O jogador jogou {(opcoes[jogador])}')

if computador == 0: #computador jogou pedra
    if jogador == 0:
        print('Pedra com Pedra, EMPATE!')

    elif jogador == 1:
        print('Papel com Pedra, Vitoria do Computador')

    elif jogador == 2:
        print('Tesoura com Pedra, Vitoria do Jogador')

    else:
        print('Algo de errado')

elif computador == 1:#computador jogou papel
    if jogador == 0:
        print('Papel com Pedra, Vitoria do Computador')

    elif jogador == 1:
        print('Papel com Papel, EMPATE!')

    elif jogador == 2:
        print('Papel com Tesoura, Vitoria do Jogador')

    else:
        print('Algo de errado')

elif computador == 2:#computador jogou tesoura
    if jogador == 0:
        print('Tesoura com Pedra, Vitoria do Jogador')

    elif jogador == 1:
        print('Tesoura com Papel, Vitoria do Computador')

    elif jogador == 2:
        print('Tesoura com Tesoura, EMPATE!')

    else:
        print('Algo de errado')




'''if jogada == 1:
    Pedra2 = jogada

elif jogada == 2:
    Papel2 = jogada

elif jogada == 3:
    Tesoura2 = jogada

Sorteio = ['Pedra' , 'Papel' , 'Tesoura']
Random_Numero = random.choice (Sorteio)

print(Random_Numero)



if jogada == Random_Numero:
    print('EMPATE!')

else :
    print('Teste')

if jogada == 1 or jogada == 2 or jogada == 3:
        print(f'{Rnumero}')

print(f'{Rnumero}')

if jogada == 1 and Rnumero == 2:
        print('Perdeu, Papel vence pedra')
'''
