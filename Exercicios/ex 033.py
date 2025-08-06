x=int(input('Primeiro Valor: '))
y=int(input('Segundo Valor: '))
z=int(input('Terceiro Valor: '))

menor=x
if y<x and y<z:
    menor=y
if z<x and z<y:
    menor=z

maior=z
if x>z and x>y:
    maior=x
if y>z and y>x:
    maior=y

print(f'O maior resultado é {maior} e o menor é {menor}')