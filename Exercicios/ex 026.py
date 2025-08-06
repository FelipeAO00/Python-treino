frase = input('Digite uma frase: ').strip()
letra = frase[0]
print(f'A primeira letra {letra} aparece {frase.upper().count(letra.upper())} vezes')
print(f'A primeira letra {letra} apareceu na posicao {frase.upper().find(letra.upper()) + 1}')
print(f'A ultima letra {frase[0]} apareceu na posicao {frase.upper().rfind(letra.upper()) + 1}')

'''
frase=str(input('Digite uma frase: ')).strip()
dividido= frase.split()
print(f'A letra {frase[0]} aparece {frase.upper().count('A')} vezes')
print(f'A primeira letra {frase[0]} apareceu na posicao {frase[0]}')
print(f'A ultima letra {frase[0]} apareceu na posicao {len(frase)}')'''