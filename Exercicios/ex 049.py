soma = 0  # Cria uma variável chamada 'soma' e atribui o valor 0 (será usada aqui apenas para somar com c no loop)

n = int(input('Digite um numero para gerar sua tabuada '))
# Pede ao usuário para digitar um número e converte para inteiro

for c in range(1, 11):
    # Cria um loop que começa no 1 e vai até 10 (range para a tabuada)

    print(n, 'x', soma + c, '=', (n * (soma + c)))
    # Mostra na tela: o número digitado, o símbolo 'x', o valor de (soma + c),
    # o sinal '=', e o resultado da multiplicação n * (soma + c


'''

num = int(input('Digite um numero para gerar sua tabuada '))
for c in range(1, 11):
        print(num, 'x', c, '=', num*c)
        
'''