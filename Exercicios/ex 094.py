"""
Exercício Python 094: Crie um programa que leia nome, 
sexo e idade de várias pessoas, 
guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. 

No final, mostre: 
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média
"""

def main():
#================================================================================================================================================
    print("Sistema de cadastro")
    cadastro = dict()
    listagem = list()
    print()
#================================================================================================================================================    
    while True:
        try:
            cadastro['nome'] = str(input("Digite o nome -> ")).title().strip()
            while True:
                cadastro['sexo'] = str(input("Digite o sexo [M/F] -> ")).strip().capitalize()

                if cadastro['sexo'] not in ["M","F"]:
                    print("Erro! Por favor, insira apenas 'M' ou 'F'. ")

                else:
                    break    

            cadastro['idade'] = int(input("Digite a idade -> "))
            
            listagem.append(cadastro)
            cadastro = {}                
    
            continuar = str(input("Deseja continuar? [S/N] -> ")).strip().capitalize() 
                        
            if continuar not in ["S","N"]:
                print("Erro! Responda apenas 'S' ou 'N'. ")

            elif continuar == "N":
                break
               
        except ValueError:
            print("Erro! Algum valor invalido foi inserido. Tente novamente. ")
            print()
#================================================================================================================================================
    print("-=" * 40)

    print(cadastro)
    print(listagem)

    total_pessoas = len(listagem)
    soma_idades = sum(pessoa['idade'] for pessoa in listagem)
    media_idade = soma_idades / total_pessoas 
    lista_mulheres = (mulheres['F'] for mulheres in listagem)
    lista_acima_media = None

    print(total_pessoas)
    print(soma_idades)
    print(media_idade)
    print(lista_mulheres)
    print(lista_acima_media)
#================================================================================================================================================
    print("-="*40)

    print(f"A) O total de pessoas cadastradas são {total_pessoas} ")

    print(f"B) A média de idade das pessoas registradas são {media_idade} ")

    print(f"C) total de mulheres cadastradas são {lista_mulheres} ")

    print(f"D) As pessoas que estão acima da media de idade são {lista_acima_media} ")
    
#================================================================================================================================================
main()