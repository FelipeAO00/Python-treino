"""
Exercício Python 092: Crie um programa que leia nome, 
ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. 
Se por acaso a CTPS for diferente de ZERO, 
o dicionário receberá também o ano de contratação e o salário. 
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
"""

def main():
    from datetime import datetime
    cadastro = dict()
    cadastro['sexo'] = ''
    ano_atual = datetime.now().year
    idade_aposentadoria_homem = 65
    idade_aposentadoria_mulher = 62
    tempo_minimo_contribuicao_homem = 35    
    tempo_minimo_contribuicao_mulher = 30
#================================================================================================================================================

    while True:
        try:
            cadastro['nome'] = str(input("Digite o seu nome: ")).strip().title()
            while cadastro['sexo'] not in ["H" , "M"]: 
                cadastro['sexo'] = str(input("Digite seu sexo: ['H' para Homem / 'M' para mulher] ")).strip().upper()
            ano_nascimento = int(input("Digite seu ano de Nascimento: "))
            cadastro['carteira_trabalho'] = int(input("Digite o numero da carteira [Digite '0' caso não tenha]: "))
    
            if cadastro['carteira_trabalho'] != 0:
                cadastro['ano_contratação'] = int(input("Digite o ano que foi contratado: "))
                tempo_contribuicao = ano_atual - cadastro['ano_contratação']
                cadastro['salario'] = float(input("Digite seu salario: "))
                print()

            break
        
        except ValueError:
            print("Algum valor foi digitado de forma invalida. Tente novamente.")
            print()
#================================================================================================================================================

    print(40*"=")
    
    cadastro['idade'] = ano_atual - ano_nascimento 

    if cadastro['sexo'] == 'H': #Homem

        idade_aposentadoria = idade_aposentadoria_homem

        tempo_minimo_contribuicao = tempo_minimo_contribuicao_homem

        anos_faltantes_idade = max(0, idade_aposentadoria - cadastro['idade'])

    elif cadastro['sexo'] == 'M': #Mulher

        idade_aposentadoria = idade_aposentadoria_mulher

        tempo_minimo_contribuicao = tempo_minimo_contribuicao_mulher

        anos_faltantes_idade = max(0, idade_aposentadoria - cadastro['idade'])

    if cadastro['carteira_trabalho'] != 0:
        tempo_faltante_contribuicao = max(0, tempo_minimo_contribuicao - tempo_contribuicao) 
        anos_faltantes = max(anos_faltantes_idade, tempo_faltante_contribuicao) 
    else:
        anos_faltantes = anos_faltantes_idade

    ano_aposentadoria = ano_atual + anos_faltantes

    cadastro['idade_aposentadoria'] = cadastro['idade'] + anos_faltantes

    ano_aposentadoria_sem_carteira  = ano_atual + anos_faltantes

    cadastro['idade_aposentadoria'] = cadastro['idade'] + anos_faltantes
     
#================================================================================================================================================

    print(f"- O nome do usuario é {cadastro['nome']} ")

    print(f"- {cadastro['nome']} tem {cadastro['idade']} anos ")

    if cadastro['carteira_trabalho'] != 0:
        print(f"- O CTPS tem valor de '{cadastro['carteira_trabalho']}' ")

    if cadastro['carteira_trabalho'] != 0:
        print(f"- O seu ano de contratação foi {cadastro['ano_contratação']}")

    if cadastro['carteira_trabalho'] != 0:
        print(f"- Seu salario é R${cadastro['salario']:.2f}")
        print(f"- Sua aposentadoria sera daqui {anos_faltantes} anos, no ano de {ano_aposentadoria}")

    if cadastro['carteira_trabalho'] == 0:
        print(f"- Sua aposentadoria caso voce pague sempre o INSS sera daqui {anos_faltantes}, no ano de {ano_aposentadoria_sem_carteira}")

main()