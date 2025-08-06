import random
n1=str(input('Digite o um nome '))
n2=str(input('Digite o um nome '))
n3=str(input('Digite o um nome '))
n4=str(input('Digite o um nome '))

alunos= [n1,n2,n3,n4]
random.shuffle(alunos)
print(f'A ordem do sorteio foi {alunos} ')

'''import random
a1 = str(input("Digite o nome do 1º aluno: "))
a2 = str(input("Digite o nome do 2º aluno: "))
a3 = str(input("Digite o nome do 3º aluno: "))
a4 = str(input("Digite o nome do 4º aluno: "))

alunos = [a1, a2, a3, a4 ]

random.shuffle(alunos)

print(f"A ordem de apresentação será: \n{alunos}")'''

