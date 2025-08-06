num=int(input('Digite um numero: '))

print('''Escolha a base de conversao
Digite 1 para binario
Digite 2 para Octal
Digite 3 para Hexadecimal''')
opcao=int(input('sua opcao e?: '))
if opcao==1:
    print(f'Seu numero e {num} e ele em binario e {bin(num)[2:]}')
elif opcao==2:
    print(f'Seu numero e {num} e ele em octal e {oct(num)[2:]}')
elif opcao==3:
    print(f'Seu numero e {num} e ele em Hexadecial e {num, hex(num)[2:]}')