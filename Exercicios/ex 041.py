print('Analise de categoria')
n=int(input('Digite sua idade para avancar: '))
if n <= 9:
    print('Voce esta na categoria mirim')
elif n <=14:
    print('voce esta na categoria infantil')
elif n <=19:
    print('voce esta na categoria Junior')
elif n <=25:
    print('voce esta na categoria Senior')
elif n >25 :
    print('voce esta na categoria Master')