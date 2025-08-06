import random
numero=random.randint(0,5) # Sorteia um número inteiro entre 0 e 5
print('Vou pensar em um numero de 0-5. Tente advinhar...')
Meu=int(input('Em que numero eu pensei?: ')) # Converte o input para inteiro

if numero == Meu:
    print(f'Boa, pensei no numero {numero}')
else:
    print(f'BURRO! pensei no numero {numero}')