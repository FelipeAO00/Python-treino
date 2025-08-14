
print('Numeros pares') # Exibe o título na tela


# Loop que percorre todos os números de 1 até 50 (o último valor do range é excluído)
for n in range(1,51):

    # Verifica se o número é par (resto da divisão por 2 igual a zero)
    if n % 2 == 0:
        # Imprime o número, ficando na mesma linha por causa do "end=' '"
        print(n, end =' ')



'''
print('Numeros pares')

for n in range(2, 51, 2):
    print('.', end= ' ')
    print(n, end =' ')

'''