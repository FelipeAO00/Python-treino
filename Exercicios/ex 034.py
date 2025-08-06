salario=int(input('Digite seu salario para o calculo do aumento: '))
quinze= salario*15 /100
dez=salario*10 /100
if salario<=1250 :
    print(f'Seu salario teve um acrescimo de R${quinze} e o total dele agora é R${quinze+salario} ')
else:
    print(f'Seu salario teve um acrescimo de R${dez} e o total dele agora é R${dez+salario} ')
