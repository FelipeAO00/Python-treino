"""
Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
"""

lista = []

X = input("Digite uma expressão. O programa ira valida-la: ")
lista.append(X)

if "()" in lista:
    if "()"  %2 == 0:
        print("Expressão VALIDA! ")
    else:
        print("Expressão INVALIDA! ")
