palavra = input("Digite uma palavra para verificar se é um palíndromo: ")

if palavra == palavra[::-1]:
    print("A palavra é um palíndromo.")
else:
    print("A palavra não é um palíndromo.")
