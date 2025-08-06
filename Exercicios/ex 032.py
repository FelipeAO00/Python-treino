'''Para saber se um ano será bissexto, basta que ele seja divisível por 4.
O ano de 2016, por exemplo, é divisível por 4. Logo, é bissexto.
Mas para anos centenários (1900, por exemplo) a regra é que ele seja divisível por 400
para que o mês de fevereiro tenha um dia a mais.'''

from datetime import date
ano=int(input('Digite o ano para descobrir se e bissexto: '))
if ano ==0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 !=0 or ano % 400 ==0 :
    print(f'O Ano {ano} é bissexto!')
else:
    print(f'O Ano {ano} não é bissexto!')
