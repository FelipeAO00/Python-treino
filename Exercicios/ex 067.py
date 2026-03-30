#Exercício Python 067: Faça um programa que mostre a tabuada de vários números, 
#um de cada vez, para cada valor digitado pelo usuário. 
#O programa será interrompido quando o número solicitado for negativo. 
print("Programa de Tabuada [Digite N negativo para sair]")
print("")
while True:
    
    n = int(input("Digite um numero para ver a tabuada: "))
    if n < 0:
        break
    print("=" *40)
    for t in range(1,11):
        print(f"{n} x {t} = {n*t}")
    print("=" *40)
print("Tabuada encerrada!")