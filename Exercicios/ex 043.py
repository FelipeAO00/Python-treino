"""Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

IMC abaixo de 18,5: Abaixo do Peso
Entre 18,5 e 25: Peso Ideal
25 até 30: Sobrepeso
30 até 40: Obesidade
Acima de 40: Obesidade Mórbida"""

print('Calculadora de IMC')
print('                  ')
peso=float(input('Digite seu peso: '))
altura=float(input('Digite sua altura: '))

imc= peso/altura**2

if imc <= 18.5 :
    print(f'Seu imc esta em {imc :.2f}, abaixo do peso')

elif 18.5 <= imc < 25 :
    print(f'Seu imc esta em {imc :.2f}, esta no peso ideal')

elif 25 <= imc < 30 :
    print(f'Seu imc esta em {imc :.2f}, esta com sobrepeso')

elif 30 <= imc < 40 :
    print(f'Seu imc esta em {imc :.2f}, esta no peso com obsidade')

elif imc >= 40 :
    print(f'Seu imc esta em {imc :.2f}, esta com obsidade morbida')

