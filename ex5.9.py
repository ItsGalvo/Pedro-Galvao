nomes = input("Digite uma lista de nomes separados por espaço: ").split()

nomes_caixa_alta = list(map(str.upper, nomes))

print("Lista com os nomes em caixa alta:", nomes_caixa_alta)
