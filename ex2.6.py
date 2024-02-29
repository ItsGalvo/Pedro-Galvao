frase = input("Digite uma palavra/frase: ")

fraseinvertida = frase[::-1]

if fraseinvertida == frase:
    print("É um palíndromo")

else:
    print("Não é um palíndromo")