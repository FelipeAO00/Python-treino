"""
Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
"""

expressao = True
lista = []

programa = input(
    "Digite uma expressão. O programa irá analisar o uso de parênteses: "
)

for varredura in programa:

    if varredura == "(":
        lista.append("(")

    elif varredura == ")":

        if len(lista) == 0:
            expressao = False

        else:
            lista.pop()

if len(lista) > 0:
    expressao = False

if expressao:
    print("Expressão Válida!")

else:
    print("Expressão Inválida!")