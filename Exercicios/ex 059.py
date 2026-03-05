"""Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
"""
run = True
while run:
    print("Iniciando calculadora")
    
    V1 = int(input("Digite o primeiro valor: "))
    
    V2 = int(input("Digite o segundo valor: "))
    
    print("selecione uma acao: ")
    acao = int(input("""
        [ 1 ] somar
        [ 2 ] multiplicar
        [ 3 ] maior
        [ 4 ] novos números
        [ 5 ] sair do programa
        [   ] Insira o numero <-- """))
                    #calculadora

    #soma
    if acao == 1:
        resultado =  V1  +  V2
        print(f"A soma entre {V1} e {V2} é: {resultado}")
        

    #mult
    elif acao == 2:
        resultado = V1 * V2
        print(f"o resultado entre {V1} x {V2} é: {resultado}")
        

    #qual e o maior
    elif acao == 3:
        if V1 < V2:
            resultado = V2
        else:
            resultado = V1
        print(f"O maior numero entre {V1} e {V2} é {resultado}")

    #inserir numero novamente
    elif acao == 4:
        print("informe os numeros novamente")
        V1 = int(input("Digite o primeiro valor: "))
    
        V2 = int(input("Digite o segundo valor: "))
            
    #encerrar
    elif acao == 5:
        print("Encerrando")
        run = False

    else:
        print("Opcao invalida tente novamente")

print("=*=" * 10)