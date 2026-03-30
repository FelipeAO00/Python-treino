#Exercício Python 62: Melhore o DESAFIO 061, 
# perguntando para o usuário se ele quer mostrar mais alguns termos. 
# O programa encerrará quando ele disser que quer mostrar 0 termos.
"""
EX 51
print('PROGRESSAO ARITIMETICA 10 NUMEROS')

termo=int(input('Digite o primeiro termo da PA '))

razao=int(input('Digite a razao da PA '))

quantidade_termos = razao*10

for c in range(termo, quantidade_termos , razao):
    print(c)
EX 61
qt = 1
print("=" * 10,"Gerador de P.A", "=" *10)
termo = int(input("Digite o primeiro termo da P.A: "))
razao = int(input("Digite a razao da P.A: "))
for q in range(10):
    print(termo, end=" --> ",)
    termo += razao
    qt += 1
print("FIM.")
"""
t = 0
qt = 0
more = 10
print("=" * 10,"Gerador de P.A", "=" *10)
termo = int(input("Digite o primeiro termo da P.A: "))
razao = int(input("Digite a razao da P.A: "))
while more != 0:
    t =  t + more
    while qt != t:
        print(termo, end=" --> ",)
        termo += razao
        qt += 1
    print("Pausa")
    more = int(input("Quantos termos voce quer mostrar mais? [] <--"))
print("Fim.")
