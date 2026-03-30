#Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado. 
#No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
#O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
run = True

menor = maior = total = cont = 0
while run:
    n = int(input("Digite um numero: "))
    total += n
    cont += 1
    if maior < n:
        maior = n
    if menor == 0 or menor > n:
        menor = n
    r = str(input("Deseja continuar? [S/N] ")).lower().strip()
    #if r  != str:
    #    r = str(input("Numero detectado, Digite novamente! [S/N] ").lower().strip())
    if r == "n":
        run = False
print(f"{cont} cont, {total/cont} media")
print(f"{maior} e {menor}")
