#ex Exercício Python #053 - Detector de Palíndromo

print("Verificador de Palindromos")

palavra = str(input("Digite uma palavra: ")).strip().upper()


inversor = palavra[::-1]
print(f"sua palavra e {palavra} e invertida fica {inversor}")

if palavra == inversor:
    print("A sua palavra e um palidromo")
else:
    print(f"sua palavra {palavra} nao e um palindromo")