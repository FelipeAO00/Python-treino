"""
Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
Caso o número já exista lá dentro, ele não será adicionado. 
No final, serão exibidos todos os valores únicos digitados, em ordem crescente. 
"""

print("Programa iniciado")

lista = []

while True:
    
    v = int(input("Digite um valor a ser registrado: "))
    
    if v in list:
        print(f"O valor {v} ja foi registrado, insira outro.")

                #  Nao funciona com o "if" apenas com "try" e "except"
    #elif v == str:
        #v = int(input("Elemento invalido. Digite um NUMERO para ser registrado: "))
            

    
    #elif v == None:
          #v = int(input("Valor vazio. Digite um valor a ser registrado: "))

    else:
        list.append(v)
        print(f"Valor valido registrado. [{v}]")

    r = input("Deseja continuar? [S/N]: ").strip().lower()
    
    if r == "n":
        break
         
                #  Nao funciona com o "if" apenas com "try" e "except"

    #elif r == None:
        #r = input("Valor vazio. Digite novamente para continuar [S/N]: ").strip().lower()

print()

print(f"Os valores digitados foram: {sorted(lista)}")
        
   