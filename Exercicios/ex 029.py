vel=float(input('Qual é a velocidade atual do carro? '))

if vel > 80: # Se usa  ">" ou ">=" ao invés de "=>"
    excesso = vel - 80
    multa = excesso * 7
    print(f'MULTADO! esta {excesso}! acima da velocidade permitida. \n Deve pagar um total de {multa} ')

else: # else nao precisa de variavel, ele e simplesmente tudo que nao seja if
    print('Você esta na velocidade correta! \n Continue assim.')