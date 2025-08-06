print('Calculadora de media escolar')
n1=int(input('Digite sua primeira nota: '))
n2=int(input('Digite sua segunda nota: '))
n3=int(input('Digite sua terceira nota: '))
n4=int(input('Digite sua quarta nota: '))
media=(n1+n2+n3+n4)/4

print(f"A sua media e: {media}")
if media > 7:
    print('Legal vc passou :D, aprovado')
elif media == 7:
    print("quase emKK, aprovado")
elif media < 7:
    print('BURRO, reprovado')