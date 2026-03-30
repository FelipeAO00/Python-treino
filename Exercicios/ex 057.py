#Exercício Python 057: Faça um programa que leia o sexo de uma pessoa, 
# mas só aceite os valores 'M' ou 'F'. Caso esteja errado, 
# peça a digitação novamente até ter um valor correto.
run = True

while run:
    sexo = str(input("Por favor informe seu sexo M/F: ")).upper().strip()
    
    if sexo == "M" or "F":
        print(f"Cadastro concluido, {sexo} registrado com sucesso")
        run = False
    elif sexo != "M" or "F":
        print("dados invalidos, por favor, informe seu sexo novamente ")