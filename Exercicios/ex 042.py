print('Analisador de triangulos')
x=int(input('Primeiro segmento: '))
y=int(input('Segundo segmento: '))
z=int(input('Terceiro segmento: '))

if x + y < z and z + y < x and z + x < y  :
    print('Os segmentos podem formar um triangulo')

else :
    print('Os segmentos nao podem formar um triangulo')
    (exit())

if x == y == z :
    print('Os segmentos sao iguais, e um triangulo equilatero.')

elif x == y !=z or y == z != x or x == z != y :
    print('Dois segmentos sao iguais, e um triangulo isosceles')

elif x != y != z :
    print('Os segmentos sao diferentes, e um triangulo escaleno')

else:
    print('Nao representa um triangulo')

'''x + y < z and z + y < x and z + x < y  :

x + y > z and z + y > x and z + x > y :'''