#perguntar o valor da casa
#o salario do comprador
#quantos anos ele vai pagar
#a prestacao nao pode passar de 30%

valor_casa=float(input('Quanto e o valor da casa?: '))
Salario=float(input('Quanto voce ganha?: '))
anos=int(input('Quantos anos voce planeja pagar: '))

conta=valor_casa/anos
conta2=conta*30/100

if conta2 > Salario:
    print('nao e possivel pagar')
else:
    print('pode pagar')
