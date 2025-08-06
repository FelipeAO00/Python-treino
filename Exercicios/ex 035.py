
print('Analisador de triangulos')
x=int(input('Primeiro segmento: '))
y=int(input('Segundo segmento: '))
z=int(input('Terceiro segmento: '))

if x+y >z and z+y>x and z+x>y :
    print('Os segmentos podem formar um triangulo')
else:
    print('Os segmentos nao podem formar um triangulo')
