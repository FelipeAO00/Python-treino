# Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint

tuple = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))

print(f"Os numero sorteados foram {tuple}")
print(f"O maior numero e o menor numero sorteado foram, respectivamente: {max(tuple)} , {min(tuple)}")