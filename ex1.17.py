preco_mercadoria = float(input("Digite o preço da mercadoria: "))
desconto = float(input("Digite o desconto (em %): ")) / 100
imposto = float(input("Digite o imposto (em %): ")) / 100

preco_final = preco_mercadoria * (1 - desconto) * (1 + imposto)

print("O preço final da mercadoria é:", preco_final)