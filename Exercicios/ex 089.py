"""
Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. 
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
"""

def main():

    Boletim = []

    while True:
        try:
            # cadastro de nome e notas do aluno.
            aluno_nome = str(input("Digite o nome do aluno: ")).strip().title()
        
            aluno_nota1 = float(input("Digite a nota do 1º semestre: "))
        
            aluno_nota2 = float(input("Digite a nota do 2º semestre: "))

            media = (aluno_nota1 + aluno_nota2) / 2
            Boletim.append([aluno_nome, [aluno_nota1,aluno_nota2], media])

            quebra = str(input("Deseja continuar? [S/N]: ")).strip().lower()

            if quebra not in ["s","n"]:
                print("Erro! Valor invalido. Digite 'S' ou 'N' ")

            elif quebra == "n":
                break
                

        except ValueError:
            print("Erro! Algum valor invalido foi digitado. Tente novamente. ")
            print()


    print("="*40)

    print(f"{'Num':>5} {'Nome':^15} {'Media':<5}")
    for i , a in enumerate(Boletim):
        print(f"{i:>5} {a[0]:^15} {a[2]:<5}")

    print("="*40)

    while True:
        try:
            print()
            quebra = int(input(f"Deseja ver os dados de algum aluno?\nDigite o numero de registro! [999 para parar!] "))
            print()
            if quebra == 999:
                print()
                print("Encerrando programa...")
                print()
                break

            if quebra > 999:
                print("Voce quis dizer '999'? ")

            if 0 <= quebra < len(Boletim):
                print()
                print(f"Notas de {Boletim[quebra][0]} são {Boletim[quebra][1]} com media de {Boletim[quebra][2]} ")
                print()

            else:
                print("Erro! Aluno não encontrado/registrado.")
                print()
        except ValueError:
            print("Erro! Algum valor invalido foi digitado. Tente novamente. ")
            print()
            
    print("="*40)



main()