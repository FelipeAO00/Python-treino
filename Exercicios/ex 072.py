#Exercício Python 072: 
#Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. 
#/Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
tuple =("zero","um","dois","três","quatro","cinco","seis","sete","oito","nove","dez",
        "onze","douze","treze","quatorze","quinze","dezesseis","dezessete","dezeoito",
        "dezenove","dezevinte")
while True:
    numero = int(input("Digite um numero: [Entre 0 e 20] "))
    while numero < 0 or numero > 20:
        numero = int(input("Valor invalido! Digite um numero novamente: [Entre 0 e 20] "))
    for insersao in range(1):
        print(f"Voce digitou o numero {tuple[numero]}")