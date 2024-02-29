nomes = input("Digite uma lista de nomes separadas por espaço: ").split()
idades = input("Digite uma lista de idades separados por espaço: ").split()

dicionario = dict(zip(nomes, idades))

# Imprime o dicionário resultante
print("Dicionário resultante:", dicionario)
