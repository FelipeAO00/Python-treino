from math import hypot

num=float(input('Digite o cateto oposto: '))
num2=float(input('Digite o cateto adjacente: '))
'''C= num**2 + num2**2
print(f'a Hipotenusa vai medir {C**(1/2):.2f} ')'''
print(f'a hipotenusa vale: {hypot(num, num2):.2f}')