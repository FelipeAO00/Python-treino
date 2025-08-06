'''nome com todas as letras maiuscolas
o nome com todas minusculas
quantas letras ao todo sem contar os espaços
quantas letras tem o primeiro nome'''
Nome= str(input('qual o seu nome: '))
print(f'Seu nome em maiusculo é: {Nome.upper()}')
print(f'Seu nome em minusculo é: {Nome.lower():}')
print(f'Seu nome tem {len(Nome.strip())} letras: ')
dividido= Nome.split()
print(f'Seu primeiro nome é {dividido[0]} e ele tem {len(dividido [0])} letras ')