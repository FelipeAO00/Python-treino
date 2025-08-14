#Exercício Python 050: Desenvolva um programa que leia seis números inteiros e mostre a
# soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

soma = 0  # Variável que vai acumular a soma dos números pares digitados

# Loop que vai se repetir 6 vezes (de 1 até 6, pois o range exclui o último número)
for c in range(1, 7):
    n = int(input('Digite um numero: '))  # Pede para o usuário digitar um número inteiro

    # Verifica se o número é par (resto da divisão por 2 igual a 0)
    if n % 2 == 0:
        soma = soma + n  # Adiciona o número à variável 'soma'

    # Caso não seja par, verifica se é múltiplo de 3
    elif n % 3 == 0:
        print(end='')  # Não faz nada visível, só mantém a estrutura do if/elif

# Exibe o valor final da soma
print(f'{soma}')

