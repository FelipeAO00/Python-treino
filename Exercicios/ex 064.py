#Exercício Python 064: Crie um programa que leia vários números inteiros pelo teclado. 
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
# No final,mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
total = 0
cont_n = 0
run = True
while run:
    n = int(input("Digite um numero! [999 para parar]: "))
    total += n
    cont_n += 1
    if n == 999:
        cont_n -= 1
        total -= 999
        run = False
print(f"O total de numeros digitados foi {cont_n}, e a soma entre eles é {total}")