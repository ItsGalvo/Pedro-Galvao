numeros = input("Digite a lista de números separados por espaço: ").split()

for i in range(0, len(numeros), 2):
    if i + 1 < len(numeros):
        numeros[i], numeros[i + 1] = numeros[i + 1], numeros[i]

print("Lista com os elementos de índices pares invertidos:", numeros)
