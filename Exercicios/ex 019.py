import random
nome1=str(input('Digite o nome do aluno: '))
nome2=str(input('Digite o nome do aluno: '))
nome3=str(input('Digite o nome do aluno: '))
nome4=str(input('Digite o nome do aluno: '))
alunos=nome1,nome2,nome3,nome4

print(f'O aluno sorteado foi {random.choice(alunos)}')