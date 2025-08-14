soma = 0
cont = 0
for n in range(3, 501 , 2 ):
    if n % 3 == 0 :
        soma = soma + n
        cont = cont + 1
print(f'A soma de todos os numeros e {soma} e a quantidade de numeros somados foi {cont}', end= ' ')
