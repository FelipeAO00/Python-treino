Viagem=float(input('Digite a distancia da viagem em KM: '))

if Viagem<=200:
    print(f'O valor da viagem é de {0.50*Viagem}R$: ')
else:
    print(f'O valor da viagem é de {0.45*Viagem}R$: ')