from datetime import date

print('ANALISE DE IDADE PARA ALISTAMENTO MILITAR')
idade=int(input('Digite sua idade: '))
ano_atual = date.today().year
minimo = 18
nasc=ano_atual-idade

if idade < minimo:
    print(f'Vai chegar tua hr mlk... falta so {minimo - idade} anos hehe. voce vai ter q se alistar em {nasc+minimo} ')
elif idade > minimo:
    print(f'Passou da idade doidao,Se alistou/devia se alistar a {idade - minimo} anos')
elif idade == minimo:
    print('Esta na hora de se alistarkk')