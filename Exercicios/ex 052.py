'''n=int(input('Digite seu numero: '))
print(f'Seu numero e {n}')


for p in range (1 , (n +1)):
   if n % p == 0:
       print(f'O numero {n} primo')'''


num = int(input("Digite um número: "))
contador = 0

for i in range(1, num + 1):
    if num % i == 0:
        contador += 1

print(f"O número {num} foi divisível {contador} vezes!")

if contador == 2:
    print("O número é primo")
else:
    print("O número não é primo")