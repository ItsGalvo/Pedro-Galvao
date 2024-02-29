numeros = input("Digite uma lista de números separados por espaço: ").split()

numeros = list(map(int, numeros))

quadrados = list(map(lambda x: x ** 2, numeros))

print("Lista com os quadrados de cada número:", quadrados)
