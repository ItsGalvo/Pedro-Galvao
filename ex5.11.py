numeros = input("Digite uma lista de números separados por espaço: ").split()

numeros = [int(numero) for numero in numeros]

pares = [numero for numero in numeros if numero % 2 == 0]

print("Números pares:", pares)
